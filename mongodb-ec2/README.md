## Neste módulo, foi realizada a criaçao de uma instância no [AWS EC2](https://us-east-2.console.aws.amazon.com/ec2/home?region=us-east-2), e posteriormente, o acesso a essa mesma instância pelo terminal, via SSH. Foi criado então um banco de dados com o [MongoDB](https://www.mongodb.com/pt-br), e realizadas algumas operações de inserção de dados, alterações e consultas, para fixar o aprendizado. 

### Fluxograma:  

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/57853741-f0a3-48e5-b50c-d00ac03dbdf9)

### Passo a Passo:  

1) Acesse o EC2 na AWS e realize a criação de uma nova instância.  

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/ff57e8c4-657d-41d3-9381-7153f39188bf' height='300'/>
<div/><br>  
  
  * Selecione a máquina com UBUNTU, de preferência versão 20.04.  
  * Selecione a opção de gerar um par de chaves e a salve na sua máquina.<br>

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/3cb8b6ee-a3d0-4d62-9a2b-5b7edf985a24' height='350'/>
<div/><br>      

* Ajuste as configurações de rede e segurança, permitindo o tráfego SSH e finalize a criação da instância.<br>

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/540d5899-2c49-4673-9207-4f0a4f4cf428' height='350'/>
<div/><br>  

2) Após a instância subir,  vamos nos conectar pelo terminal, via SSH. No EC2, ao selecionar a opção de se conectar à instância, é possível selecionar algumas opções. Selecione "Cliente SSH" para verificar os parâmetros necessários. O exemplo que ele fornece já deve funcionar, caso vc esteja com o terminal aberto no diretório em que se encontra a chave na sua máquina

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/ff820482-3244-4601-93da-58c1bc5d495c' height='350'/>
<div/><br> 

3) Com a conexão estabelecida, baixe o unzip no terminal:
  * sudo ap-get install unzip<br>

4) Depois, crie um diretório (mkdir nomeDaPasta) e baixe o arquivo do mongo nesse diretório:<br>
  * wget https://www.datascientist.com.br/engdados/mongo.zip<br>
5) Realize a descompactação do arquivo baixado:<br>
  * unzip mongo.zip<br>

6) Altere as permissões de acesso do arquivo descompactado:<br>
* chmod 777 mongo.sh<br>

7) Execute o comando abaixo para executar o arquivo, como um bash:<br>
* ./mongo.sh<br>

8) Após isso, o MongoDb está instalado no servidor. Podemos interagir com ele por meio docomando **mongosh**:<br>

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/c9cd416d-6f03-4321-94a6-9d93f0bced19' height='350'/>
<div/><br> 

9) Para criação do banco de dados, collection e consultas, foram utilizados os seguintes scripts:

    * [Scripts](https://github.com/micvet/curso-eng-dados-fa/blob/main/mongodb-ec2/scripts/Scripts%20utilizados.pdf)<br>
  
10) Para popular a collection, foram utilizados dados fakes:
    * [Dados](https://github.com/micvet/curso-eng-dados-fa/blob/main/mongodb-ec2/dados/dados.json)<br>
   
11) Por fim, utilizamos o mongoimport para importar dados de um [JSON](https://github.com/micvet/curso-eng-dados-fa/blob/main/mongodb-ec2/dados/posts.json) e popular um banco de dados. Para isso, foi necessário sair da sessão do mongosh e digitar o seguinte comando no terminal da instância:<br>
    *mongoimport -d NomeDoBD  --legacy -c NomeDaCollection --file=NomeDoArquivo <br>

Os parâmetros que foram utilizados indicam, respectivamente:

   * Nome do BD de destino (se nao existir, será criado);
   * Legacy se refere ao formato do arquivo de importação, que é legado;
   * Nome da coleção
   * Nome do arquivo que será importado. Caso não esteja na pasta em que o arquivo está, será necessário incluir o diretório completo<br>

   <div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/122ac20b-e31a-480a-aedc-265c92c59444' height='50'/>
<div/><br> 

   Existem vários parâmetros que podem ser utilizados na importação. Para verificá-los, use mongoimport --help.<br>

12) Após realizada a importação, podemos nos conectar novamente ao mongosh e verificar os dados inseridos:

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/d6f946c6-88a2-430e-81e5-71ccea2036b7' height='350'/>
<div/><br> 












