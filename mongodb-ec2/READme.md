## Neste módulo, realizamos a criaçao de uma instância no [AWS EC2](https://us-east-2.console.aws.amazon.com/ec2/home?region=us-east-2), e posteriormente, acessamos essa mesma instância pelo terminal, via SSH. Criamos então um banco de dados com o [MongoDB](https://www.mongodb.com/pt-br) e realizamos algumas operações para fixar o aprendizado. 

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

9) Existem vários comandos que podemos utilizar.









