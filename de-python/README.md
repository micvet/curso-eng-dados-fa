## Engenharia de dados com Python

Neste módulo, criamos um script simples para testar o acesso ao bucket e a um banco de dados, ambos na plataforma AWS, no S3 e RDS, respectivamente. Foi utilizado o Google Colab para escrever um código em Python, que permitiu a leitura de dados de arquivos presentes no bucket do S3, para que estes dados fossem salvos no banco de dados PostgreSQL do RDS.<br>

### Fluxograma: 
<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/93742217-1f62-456b-9946-088c796a62d7' height='200'/>
<div/><br> 

* **Após o uso todas as instâncias criadas foram deletadas.**
  
### Passo-a-passo:

<br> 1. Criação do bucket no S3 e ingestão dos arquivos:
   - Na plataforma AWS, busque pelo serviço S3 e selecione a opção de criar um novo bucket. Se certifique de que a opção de criptografia está desativada. 

<br> 2. Crie uma nova pasta no bucket para ingestão dos arquivos. Ao finalizar o procedimento, realize o upload dos arquivos na pasta criada.
* [Arquivos para upload](https://github.com/micvet/curso-eng-dados-fa/tree/main/de-python/arquivos)

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/387bf4a5-a66e-4439-b921-1603d16abc97' height='350'/>
<div/><br>  

<br> 3. Utilize o RDS (Amazon Relational Database Service) para criar uma instância do Postgres:

* Na barra de buscas da AWS, busque pelo RDS e selecione a opção "Criar Banco de Dados".
* Selecione a Criação Padrão, PostgreSQL e modelo de nível gratuíto.
* Anote o usuário e senha que definir.
* A maioria das demais configurações podem se manter padrão. Com exceção do Acesso Público, onde deverá ser feita a seleção para "Sim".

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/bbcc3565-fe41-4fdb-a1f1-6bed10a2311a' height='250'/>
<div/><br> 
   
4) Para acesso, precisaremos do endpoint, da porta, do usuário e senha criados no banco de dados Postgress e das credencias de Chave de Acesso. <br>
* Endpoin e porta do BD:<br>

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/8f286f81-1296-4f8f-84e5-18d52caba132' height='250'/>
<div/><br>  
  
* Caso você não tenha a Chave de Acesso, pode obter uma por meio das opções de credenciais de segurança:<br>

    - Após selecionar a opção Credenciais de Segurança, role a tela até a opção Chaves de Acesso e selecione a opção de criar uma. Copie e guarde a chave de acesso e chave de acesso secreta que serão geradas.<br>
<br><div align='center'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/6996af55-60cd-452f-8535-c6d444e9a2bf' height='150'/>
<div/><br>
    
<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/978b8425-b8df-4f9d-bfb1-f95022991798' height='250'/>
<div/><br>

* As regras de segurança também devem estar habilitadas para permitir a comunicação das aplicações:<br>

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/f2fefe18-d4e6-47dc-a0a3-c2d37d53ccb3' height='170'/>
<div/><br>

5) O próximo passo é estabelecer uma conexão externa com o banco criado. Será utilizado o colab, do Google, com a linguagem Python.<br>

* Estabelecendo a conexão:
  
```
import psycopg2 #biblioteca para conectar e interagir com bd postgres
con = psycopg2.connect(host='INSIRA-O-HOST-DO-SEU-BD',database='postgres',
user='SEU-USER-DO-BD',password='SUA-SENHA-DO-BD')
con.autocommit = True #transações sendo comitadas automaticamente
cur = con.cursor() #objeto de interação com o BD 
```
* A primeira alteração que faremos é a criação de um novo banco de dados chamado "inventário:
```
cur.execute('create database inventario;')
con.close()
``` 
* Agora iremos criar a primeira tabela do nosso banco de dados. Iremos usar as mesmas credenciais que foram usadas anteriormente, mas no campo da database, 
é necessário alterar para a nova database.
```
import psycopg2
con = psycopg2.connect(host='INSIRA-O-HOST-DO-SEU-BD',database='inventario',
user='SEU-USER-DO-BD',password='SUA-SENHA-DO-BD')
con.autocommit = True
cur = con.cursor()
cur.execute('create table arquivos (idarquivo INT, nomearquivo VARCHAR(256));')
con.close()
```

6) O próximo passo é estabelecer uma conexão com o bucket. Para isso, ainda no Colab, usaremos a lib boto3. Usaremos a linguagem Shell, e para isso, basta sinalizar uma exclamação (!), antes de iniciar o comando.

```
!pip install boto3
```
* Com o boto3 instalado, vamos testar a conexão com o bucket. O objetivo é acessar o bucket e iterar nos arquivos contidos, retornando seus nomes.<br>
* Nesta etapa, serão necessários alguns dados, como a região, sua chave de acesso e chave de acesso secreta.
```
import boto3
import io
import psycopg2

s3 = boto3.resource(
    service_name='s3',
    region_name = 'sa-east-1',
    aws_access_key_id = 'SUA-CHAVE-DE-ACESSO',
    aws_secret_access_key = 'SUA-CHAVE-DE-ACESSO-SECRETA'
    )

bucket = 'mybucketcursode' #NOME DO SEU BUCKET
prefix = 'imagens/' #PASTA QUE FOI CRIADA COM OS ARQUIVOS

for objects_s3 in s3.Bucket(bucket).objects.filter(Prefix=prefix):
  if objects_s3.key.endswith('jpg') or objects_s3.key.endswith('JPG'):
    filename = objects_s3.key.split('/')[1]
    print(filename)

```  
* Agora, após verificar que a conexão é estabelecida com sucesso, iremos utilizar a conexão para ler dados nos arquivos do bucket e inseri-los no banco de dados criado anteriormente.

```
s3 = boto3.resource(
    service_name='s3',
    region_name = 'sa-east-1',
    aws_access_key_id = 'AKIA5FTZDWTFQQEKL7PR',
    aws_secret_access_key = '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'
    )

bucket = 'mybucketcursode'
prefix = 'imagens/'

con = psycopg2.connect(host='database-1.clim6smom0jt.sa-east-1.rds.amazonaws.com',database='inventario',
                       user='postgres',password='12345678')
con.autocommit = True
cur = con.cursor()
id = 0

for objects_s3 in s3.Bucket(bucket).objects.filter(Prefix=prefix):
  if objects_s3.key.endswith('jpg') or objects_s3.key.endswith('JPG'):
    filename = objects_s3.key.split('/')[1]
    print(filename)
    id += 1
    cur.execute("insert into arquivos (idarquivo,nomearquivo) values (" +str(id)+ ",'" + filename + "')") #Será gerado um id atribuido a cada item

con.close()
```

* E agora vamos verificar se os dados foram inseridos corretamente:

```
con = psycopg2.connect(host='INSIRA-O-HOST-DO-SEU-BD',database='inventario',user='SEU-USER-DO-BD',password='SUA-SENHA-DO-BD')

con.autocommit = True
cur = con.cursor()

cur.execute('select * from arquivos;')
recset = cur.fetchall() #fetchall é um método para retornar todos os dados.
for rec in recset:
  print(rec)
con.close()
```
* Resultado:
<br><div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/f71c274a-04db-477a-824b-3fbfb1b18adb' height='350'/>
<div/><br>  

* Script utilizados:
  * [Script](https://github.com/micvet/curso-eng-dados-fa/blob/main/de-python/scripts/ScriptEngDados.ipynb)   




 
