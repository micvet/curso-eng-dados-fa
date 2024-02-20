## Aplicações em Streaming - Kinesis <br>

Neste módulo, 

### Fluxograma<br>


### Sobre o Kinesis:<br>

O Amazon Kinesis é um serviço de streaming de dados em tempo real oferecido pela AWS. Ele permite a coleta, processamento e analise grandes volumes de dados de streaming em tempo real. Ele é útil em casos de uso onde é necessário processar e analisar grandes quantidades de dados em tempo real, como análise de logs, monitoramento de aplicativos, análise de fluxo de cliques, IoT (Internet das Coisas), etc.

Componentes dentro do Amazon Kinesis:

* Amazon Kinesis Data Streams: Permite a ingestão e processamento de grandes volumes de dados de streaming em tempo real.

* Amazon Kinesis Data Firehose: Facilita a ingestão de dados de streaming para armazenamento em outros serviços da AWS, como Amazon S3, Amazon Redshift e Amazon Elasticsearch.

* Amazon Kinesis Data Analytics: Permite o processamento e analise dados de streaming usando consultas SQL padrão.

* Amazon Kinesis Video Streams:  serviço para ingestão, processamento e armazenamento de vídeo de streaming para análise e aprendizado de máquina.

### Passo-a-passo do projeto:<br>

1) Primeiramente, foram criados três notebooks usando o Google Colab; um para gerar uma aplicação que irá gera os dados e enviá-los ao Kinesis e o segundo para os consumir.

2) Já na plataforma AWS, busque pelo Kinesis e crie um novo fluxo de dados selecionando a opção Kinesis Data Streams

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/74859e0f-9773-495e-90d2-255de1c26d77)

* Mantenha as opções padrão. Para fins de conhecimento, a opção de Capacidade de fluxo de dados sob demanda, se ajuta conforma a necessida, enquanto na provisionada, deve ser alterada manualmente.
* Após o stream estar ativo, podemos iniciar o fluxo de dados. 

3) Para gerar e enviar a informação, criaremos um produtor usando um dos notebooks do Colab, nomeado como Prod.
* Primeiramente vamos instalar o [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) para interagir com os serviços da AWS.
```
!pip install boto3
```
*O próximo passo é  criar uma instância do cliente para realizar autenticação na plataforma AWS:

```
cliente = boto3.client('kinesis',aws_access_key_id='SUA_CHAVE_DE_ACESSO',aws_secret_access_key='SUA-CHAVE-DE-ACESSO-SECRETA',
                       region_name='us-east-2') #substituia a região, se necessário
```

* Para o stream de dados no Kinesis, os dados têm que estar serializados no formato JSON. A melhor forma de fazer isso é por meioda criação de uma estrutura DIC no python.
```
registro = {'idvendedor' : '991', 'nome' : 'Ana' }
```
* O passo seguinte é criar a variável responsável pelo envio das informações e que trará o retorno da resposta.
```
#método put_record = faz o envio
resposta = cliente.put_record( 
                  StreamName='NOME_DO_SEU_STREAM_DO_KINESIS', 
                  Data = json.dumps(registro), #nesta variável estamos serializando o dic criado como formato JSON
                  PartitionKey='02' #Forma de dividir os dados em diferentes chaves. 
                  )
print(resposta)
```
Após executar os comandos, será gerado um ShardID, que usaremos nos próximos passos.

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/67cffe1a-f66b-4e64-a7b4-1c2df25e8372)

4) O próximo passo será criar um cliente, que receberá os dados produzidos pelo Prod.
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
* O Loop for será usado para retornar os registros do método anterior, get_records(). Ele vai iterar nos registros e printar algumas informações sobre cada um. 

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

5) Outra opção é criar outro consumidor, o Kinesis Fire House, que recebe o stream e faz a entrega. Usaremos o bucket para receber os dados produzidos.

* Primeiramente, na plataforma AWS, selecione a opção de criar um novo Kinesis Fire House.
  ![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/4fb01f32-367f-4033-88dd-d94b2945553a)





