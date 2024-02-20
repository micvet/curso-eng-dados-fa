## Aplicações em Streaming - Kinesis <br>

Neste módulo aprendemos sobre aplicações streaming e ingestão de seus dados. Criamos um fluxo de stream no AWS Kinesis Data Streams e dois programas: um responsável por gerar os dados e o segundo, por consumi-lo. Assim, os dados eram gerados no programa prod, coletados pelo Kinesis Data Streams e depois consumidos pelo programa cons1 Em alternativa a esse fluxo, criamos também um consumidor no Kinesis Firehose, que permitiu que os dados gerados pelo programa prod, fossem enviados a um bucket no S3 após serem coletados pelo Data Streams.<br>

### Fluxograma<br>

<br><div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/cda4fa22-444d-4e89-ac36-c9d3ac83ef2b' height='350'>
<div/><br>

### Sobre o Kinesis:<br>

O Amazon Kinesis é um serviço de streaming de dados em tempo real oferecido pela AWS. Ele permite a coleta, processamento e analise grandes volumes de dados de streaming em tempo real. Ele é útil em casos de uso onde é necessário processar e analisar grandes quantidades de dados em tempo real, como análise de logs, monitoramento de aplicativos, análise de fluxo de cliques, IoT (Internet das Coisas), etc.

Componentes dentro do Amazon Kinesis:

* Amazon Kinesis Data Streams: Permite a ingestão e processamento de grandes volumes de dados de streaming em tempo real.

* Amazon Kinesis Data Firehose: Facilita a ingestão de dados de streaming para armazenamento em outros serviços da AWS, como Amazon S3, Amazon Redshift e Amazon Elasticsearch.

* Amazon Kinesis Data Analytics: Permite o processamento e análise dados de streaming usando consultas SQL padrão.

* Amazon Kinesis Video Streams:  serviço para ingestão, processamento e armazenamento de vídeo de streaming para análise e aprendizado de máquina.

### Passo-a-passo do projeto:<br>

1) Primeiramente, foram criados dois notebooks usando o Google Colab; um para gerar uma aplicação que irá gera os dados e enviá-los ao Kinesis e o segundo para os consumir.<br>

2) Já na plataforma AWS, busque pelo Kinesis e crie um novo fluxo de dados selecionando a opção Kinesis Data Streams. <br>
<br><div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/74859e0f-9773-495e-90d2-255de1c26d77' height='200'>
<div/><br>

* Mantenha as opções padrão. Para fins de esclarecimento, a opção de Capacidade de Fluxo de Dados sob Demanda faz com que as configurações de fluxo se ajustem conforme a necessidade, enquanto na opção provisionada, as configurações devem ser alteradas manualmente.
  
* Após o stream estar ativo, podemos iniciar o fluxo de dados. <br>

3) Para gerar e enviar a informação, criaremos um produtor usando um dos notebooks do Colab, nomeado como prod.
* [Script](https://github.com/micvet/curso-eng-dados-fa/blob/main/app-streaming-kinesis/scripts/prod.ipynb)<br>

* Primeiramente vamos instalar o [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) para interagir com os serviços da AWS.<br>
```
!pip install boto3
```
*O próximo passo é  criar uma instância do cliente para realizar autenticação na plataforma AWS. <br>

```
cliente = boto3.client('kinesis',aws_access_key_id='SUA_CHAVE_DE_ACESSO',aws_secret_access_key='SUA-CHAVE-DE-ACESSO-SECRETA',
                       region_name='us-east-2') #substituia a região, se necessário
```

* Para o stream de dados no Kinesis, os dados têm que estar serializados no formato JSON. A melhor forma de fazer isso é por meioda criação de uma estrutura DIC no python.<br>
```
registro = {'idvendedor' : '991', 'nome' : 'Ana' }
```
* O passo seguinte é criar a variável responsável pelo envio das informações e que trará o retorno da resposta.<br>
```
#método put_record = faz o envio
resposta = cliente.put_record( 
                  StreamName='NOME_DO_SEU_STREAM_DO_KINESIS', 
                  Data = json.dumps(registro), #nesta variável estamos serializando o dic criado como formato JSON
                  PartitionKey='02' #Forma de dividir os dados em diferentes chaves. 
                  )
print(resposta)
```
Após executar os comandos, será gerado um ShardID, que usaremos nos próximos passos.<br>

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/67cffe1a-f66b-4e64-a7b4-1c2df25e8372)

4) Na sequencia, será necessário criar um cliente, que receberá os dados produzidos pelo Prod.<br>
* [Script](https://github.com/micvet/curso-eng-dados-fa/blob/main/app-streaming-kinesis/scripts/cons1.ipynb) 
* Para isso, usaremos outro notebook, onde primeiramente, iremos realizar a importação do [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

```
!pip install boto3
```
* Agora, iremos realizar a criação e a=confugração da aplicação consumidora.
* Configurando o acesso ao Kinesis para receber os dados gerados:
```
cliente = boto3.client('kinesis',aws_access_key_id='SUA_CHAVE_DE_ACESSO',aws_secret_access_key='SUA-CHAVE-DE-ACESSO-SECRETA',
                       region_name='us-east-2') #substituia a região, se necessário
```
* Usaremos o método get_shard_iterator, que obtém um iterador de fragmento para o fluxo Kinesis especificado. Esse iterador será usado para ler dados do fragmento específico do fluxo. Neste caso, ele obeterá um iterador para o shard com o ID "shardId-000000000002" (que salvamos anteriormanete) do fluxo "flow1" e começará a partir do ponto mais recente (ShardIteratorType='LATEST').

```
shard = cliente.get_shard_iterator(
            StreamName="flow1",
            ShardId = 'shardId-000000000002',
            ShardIteratorType = 'LATEST'
            )["ShardIterator"]
```
* Na sequência, criaremos um Loop while que continuará enquanto o iterador não for nulo (até que não haja mais registros para ler).
* Também usaremos o método cliente.get_records(), para obter registros do fragmento. Ele receberá como argumento o iterador atual e retornará um dicionário contendo registros e um novo iterador de fragmento que pode ser usado para recuperar registros subsequentes.
* O Loop for será usado para retornar os registros do método anterior, get_records(). Ele vai iterar nos registros e printar algumas informações sobre cada um. <br>

```
while shard is not None:
  resultado = cliente.get_records(ShardIterator=shard)
  registros = resultado['Records']
  shard = resultado["NextShardIterator"]
  for registro in registros:
    print(registro["SequenceNumber"])
    print(registro["ApproximateArrivalTimestamp"])
    print(registro["PartitionKey"])
    print(registro["Data"])
```

5) Outra opção é criar um consumidor no Kinesis Firehose, que recebe o stream e faz a entrega dos dados para outros serviços. Usaremos o bucket para receber os dados produzidos.

* Primeiramente, na plataforma AWS, selecione a opção de criar um novo Kinesis Firehose.<br>
<br><div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/4fb01f32-367f-4033-88dd-d94b2945553a' height='200'>
<div/><br>

* Selecione como origem o Amazon Kinesis Data Stream e como destino, o S3. Na configuração de origem, selecione o stream criado anteriormente. Nas configurações de destino, crie um novo bucket ou use algum criado anteriormente. Nas configurações de bloqueio do acesso público do bucket, deixe o acesso público. Por fim, selecione a opção de Criar.<br>

<br><div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/f9ca0a23-4272-4d12-a6ac-3e94dd990017' height='300'>
<div/><br>

* Após criar o serviço do Firehose com sucesso, altere as configurarações de destino para reduzir o intervalo do buffer, para que os dados sejam retornados mais rapidamente neste teste.<br>

<br><div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/5bafbc89-b330-48ad-81b0-7458a3b9ef65' height='300'>
<div/><br>


* Gere novos dados por meio do Produtor prod (Notebook do Colab). Após o tempo definido no buffer, será possível observar as produções do Prod no diretório anteriormente criado no Bucket S3.<br>

<br><div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/2f5fe31a-71aa-4006-9a68-7e12937277e5' height='300'>
<div/><br>

* Arquivo gerado:<br>

  * [Arquivo](https://github.com/micvet/curso-eng-dados-fa/blob/main/app-streaming-kinesis/resultado/KDS-S3-nilhy-2-2024-02-20-20-28-11-a55a683c-1d74-4d64-8b55-804f64e3fcaf)


