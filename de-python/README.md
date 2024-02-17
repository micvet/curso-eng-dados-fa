## Engenharia de dados com Python

### Neste módulo....

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
    


    

    




 
