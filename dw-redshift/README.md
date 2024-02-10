# Neste módulo, realizamos a criaçao de um cluster no AWS Redshift. Então, foi criado um banco de dados e tabelas, que foram populadas com dados de arquivos CSV armazenados no Bucket S3, utilizando o comando copy. Geramos uma tabela desnormalizada, utilizando conceitos da modelagem multimensional, e por fim,os dados dessa tabela foram utilizados para gerar um relatório no Google Looker Studio.


![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/30115cd0-eedf-4dfa-99ce-989f1bfa11df&size=10x100)



## Passo a passo:

1. Criação do bucket no S3 e ingestão dos arquivos CSV:
   No S3, busque pelo bucket e selecione a opção para criar um novo. 
![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/8b58b8f0-7451-4214-9d16-6091e6955136)

2. Crie uma nova pasta e realize o upload dos arquivos CSV:

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/875fe71b-7905-4016-aacb-00659f2074a6)  |  ![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/19d4bf35-4dd7-4e69-bbe0-002ca344d203)

3. Busque pelo serviço do Redshift e selecione a opçao para criar um novo cluster:

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/16273dfb-48cb-4c1f-8dbb-11f0028bbff7)

4. Configurações do cluster:

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/420d1cd7-2d7c-4561-bb3b-129da6de986f)

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/0a50a707-9631-4ed3-a3fe-8d018ef713b7)

5. Após criado, selecione o cluster e vá até a aba Editor de Consultas V2:

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/739554ae-c1a9-48ea-a142-25fa81ba2f3a)

6. Será aberto um editor de queries, que será utilizado para a criação do banco de dados e tabelas:

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/7d17ae45-1a15-4ab1-89b4-1c4efd0d49b0)

7. Utilize o arquivo disponibilizado ddl para criaçao da estrutura do BD e tabelas:

   ddl

8. Com a estrutura criada, o load dos arquivos será realizado por meio do copy. Para isso, são necessárias algumas configurações e dados dos arquivos de origem.
  - Primeiramente, crie uma chave de acesso, selecionando a opção Credenciais de Segurança nas opções da sua conta;

  ![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/6996af55-60cd-452f-8535-c6d444e9a2bf)

  - Criando chave de acesso:

  ![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/978b8425-b8df-4f9d-bfb1-f95022991798)

  - Copie a chave de acesso e a chave de acesso secreta.

9. Selecione novamente o bucket e vá até a pasta onde realizou o upload dos arquivos. Selecione cada arquivo individualmente e copie sua URI:

  ![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/b6d6eb92-18d5-4547-83ea-18efeb174dde)

10. De volta ao Redshift, utilizaremos os dados da URI, chave de acesso e chave de acesso secreta para popular as tabelas anteriormente criadas:

  - script Load Data

11. Após verificar que os dados foram devidamente carregados, crie uma tabela multidimensional, que servirá de base para a criaçao da view:

    - Tabela Desnormalizada

12. Copie o endereço do endpoint do seu cluster Redshift:
     
  ![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/ad48f6e2-d014-4787-8ebf-e4c042002150)

13. Altere as configurações de acesso e segurança:
    - Nas proprieadades do cluster> configs de rede e segurança > Ativar recurso publicamente acessível > Habilitar
     
      ![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/f9724078-c459-48d4-9e25-a2ab8c316fe2)

    - Verifique se as regras do Grupo de Segurança atendem aos requisitos para acesso externo:
   
  ![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/2cb25548-ac15-45ce-ad7e-c1b57a368ae0)

   
14. Por fim, acesse o Looker Studio do Google, selecione a opção de criar um novo relatório e selecione a opção de conectar ao Redshift. Preencha os campos solicitados:
  - No campo IP/Nome do host, cole o link do endpoint do Redshift. Apague a porta e nome do BD que estão no final, caso sejam copiados também.
  - - O formato deve ser algo como "redshift-cluster-1.ctigchcnr.us-east-2.redshift.amazonaws.com";
  - Preencha o número da porta;
  - Preencha o nome do BD em que estão as tabelas criadas;
  - Preencha os campos de usuário e senha do cluster;
  - Clique em autenticar;
  - Após a conexão ser estabelecida, selecione a tabela fato e clique em adicionar;
  - Proceda com a criação do relatório.

    ![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/4189c99b-0d4c-41fe-a3f0-b2a9f5e9decd)


15. Relatório vendas. 

    









