## Neste módulo, realizamos a criação de um cluster no [AWS Redshift](https://us-east-2.console.aws.amazon.com/redshiftv2/home?region=us-east-2#landing), onde foi desenvolvido um banco de dados e nele, tabelas que foram populadas com dados de arquivos CSV armazenados no [Bucket S3](https://s3.console.aws.amazon.com/s3/buckets?region=sa-east-1), utilizando o comando Copy. Com os dados, geramos uma tabela desnormalizada utilizando conceitos da [modelagem multidimensional](https://medium.com/@aasouzaconsult/modelagem-multidimensional-e65f02bbd60), e por fim, os dados dessa tabela foram utilizados para gerar um relatório no [Google Looker Studio](https://lookerstudio.google.com/).

**Após o uso, todos os recursos utilizados na plataforma AWS foram excluídos, por tanto, os acessos que podem estar presentes nas imagens não funcionarão**

### Fluxograma:<br>
<br><div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/42e3601e-fdbc-43e0-b701-5d69f09ab7b8'>
<div/>



## Passo a passo:

<br> 1. Criação do bucket no S3 e ingestão dos arquivos CSV:
   - No S3, crie um novo bucket. 

<br> 2. Crie uma nova pasta no bucket e realize o upload dos arquivos CSV:  
<br>[Arquivos CSV](https://github.com/micvet/curso-eng-dados-fa/tree/main/dw-redshift/dados)  

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/19d4bf35-4dd7-4e69-bbe0-002ca344d203' height='300'/>
<div/>

<br> 3. Posteriormente, busque pelo serviço do Redshift e selecione a opção para criar um novo cluster:

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/16273dfb-48cb-4c1f-8dbb-11f0028bbff7' height='80'/>
<div/>


<br> 4. Configurações do cluster:<br>

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/420d1cd7-2d7c-4561-bb3b-129da6de986f' height='300'/>
<div/><br>

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/0a50a707-9631-4ed3-a3fe-8d018ef713b7' height='600'/>
<div/>

<br> 5. Após criado, selecione o cluster e vá até a aba Editor de Consultas V2.

<br> 6. Será aberto um editor de queries, que será utilizado para a criação do banco de dados e tabelas:

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/7d17ae45-1a15-4ab1-89b4-1c4efd0d49b0' height='250'/>
<div/>

<br> 7. Utilize o arquivo disponibilizado ddl para criaçao da estrutura do BD e tabelas:

   [ddl](https://github.com/micvet/curso-eng-dados-fa/blob/main/dw-redshift/scripts/ddl.sql)

<br> 8. Com a estrutura criada, o load dos arquivos será realizado por meio do copy. Para isso, são necessárias algumas configurações e dados dos arquivos de origem.
  - Primeiramente, crie uma chave de acesso, selecionando as Credenciais de Segurança nas opções da sua conta;

<br><div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/6996af55-60cd-452f-8535-c6d444e9a2bf' height='150'/>
<div/><br>


  - Criando chave de acesso:

<br><div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/978b8425-b8df-4f9d-bfb1-f95022991798' height='250'/>
<div/>


  - Copie a chave de acesso e a chave de acesso secreta.

<br> 9. Selecione novamente o bucket e vá até a pasta onde realizou o upload dos arquivos. Selecione cada arquivo individualmente e copie sua URI:

<br> <div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/b6d6eb92-18d5-4547-83ea-18efeb174dde' height='250'/>
<div/>


<br> 10. De volta ao Redshift, utilizaremos os dados da URI, chave de acesso e chave de acesso secreta para popular as tabelas anteriormente criadas, por meio do script abaixo. Ele deve ser repetido para popular cada tabela, alterando-se os dados de URI e nome da tabela, conforme necessário:

[Load Data](https://github.com/micvet/curso-eng-dados-fa/blob/main/dw-redshift/scripts/load-data.sql)

<br>11. Após verificar que os dados foram devidamente carregados, crie uma tabela multidimensional (tabela fato), que servirá de base para a criaçao da view:

[Tabela Desnormalizada](https://github.com/micvet/curso-eng-dados-fa/blob/main/dw-redshift/scripts/tabela-desnormalizada.sql)

<br> 12. Copie o endereço do endpoint do seu cluster Redshift:

<br> <div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/ad48f6e2-d014-4787-8ebf-e4c042002150' height='200'/>
<div/>
     

13. Altere as configurações de acesso e segurança:  
   - Nas proprieadades do cluster, selecione a opção de Configurações de Rede e Segurança, depois Ativar recurso publicamente acessível e habilite a função:
   
<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/f9724078-c459-48d4-9e25-a2ab8c316fe2' height='300'/>
<div/>
     
   - Verifique se as regras do Grupo de Segurança atendem aos requisitos para acesso externo:
    
<br> <div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/2cb25548-ac15-45ce-ad7e-c1b57a368ae0' height='250'/>
<div/>

   
<br> 14. Por fim, acesse o Looker Studio do Google, selecione a opção de criar um novo relatório e selecione a opção de conectar ao Redshift. Preencha os campos solicitados:
  - No campo IP/Nome do host, cole o link do endpoint do Redshift. Apague a porta e nome do BD que estão no final, caso sejam copiados também.
     -  O formato deve ser algo como "redshift-cluster-1.ctigchcnr.us-east-2.redshift.amazonaws.com";
  - Preencha o número da porta;
  - Preencha o nome do BD em que estão as tabelas criadas;
  - Preencha os campos de usuário e senha do cluster;
  - Clique em autenticar;
  - Após a conexão ser estabelecida, selecione a tabela fato e clique em adicionar;
  - Proceda com a criação do relatório.

<br> <div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/4189c99b-0d4c-41fe-a3f0-b2a9f5e9decd' height='250'/>
<div/>

  

15. Gere um [Relatório vendas](https://github.com/micvet/curso-eng-dados-fa/tree/main/dw-redshift/relatorio-looker) , conforme necessário.

    









