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
* A maioria das demais configurações podem se manter padrão. Com exceção do Acesso Público, onde deverá ser feita a seleção para "Sim".

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/bbcc3565-fe41-4fdb-a1f1-6bed10a2311a' height='250'/>
<div/><br> 
   
* Para acesso, utilizaremos o endpoint, a porta, o usuário e senha criados. <br>

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/8f286f81-1296-4f8f-84e5-18d52caba132' height='250'/>
<div/><br>  



 
