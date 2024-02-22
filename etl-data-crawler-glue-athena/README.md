# ETL e Data Crawler com Glue e Athena<br>

Neste módulo, 

**Após o uso todos os recursos utilizados na plataforma AWS foram excluídos, por tanto, os acessos que podem estar presentes nas imagens não funcionarão**<br>
## Fluxograma:


### Sobre as aplicações utilizadas: 
* AWS Glue: é um serviço de ETL (Extract, Transform, Load) gerenciado que facilita a preparação e o carregamento de dados para análise. 
Fornece recursos para descobrir, catalogar, limpar e transformar dados.
Principais funcionalidades: 

    * Armazenamento de metadados: O Glue gera um catálogo de dados que armazena metadados sobre os dados processados. 
Isso inclui informações sobre a estrutura dos dados, esquemas, dependências e estatísticas. O catálogo de dados permite a descoberta e exploração de 
conjuntos de dados e rastreio da origem e do histórico de transformações.

    * ETL Gerenciado: Permite a criação de fluxos de trabalho de ETL sem provisionar ou gerenciar infraestrutura. 
Pode-se definir transformações usando uma interface visual ou escrevendo códigos. O Glue executa automaticamente os fluxos de trabalho, 
dimensionando a infraestrutura conforme necessário.

    * Integração com Outros Serviços da AWS: O Glue integra-se com outros serviços da AWS, como S3, Redshift, RDS, Athena e EMR. 

    * Descoberta e Catalogação Automática: O Glue pode descobrir automaticamente a estrutura e o esquema dos seus dados e catalogá-los no catálogo de dados.

* AWS Athena: Amazon Athena é um serviço de análise interativa da AWS que permite consultar dados diretamente no Amazon S3 usando SQL padrão. Não é necessário
configurar ou gerenciar infraestrutura, e pode-se executar consultas ad hoc em grandes volumes de dados armazenados no S3 sem a necessidade de carregar os dados
em um armazenamento de dados tradicional. Principais funcionalidades:

  * Consultas SQL Padrão: suporta consultas SQL padrão, permitindo a escrita de consultas para analisar dados. 

  *  Integração com o Amazon S3: é integrado diretamente com o Amazon S3, permitindo a consulta de dados armazenados em qualquer formato suportado pelo S3.

  * Escalabilidade Automática: O Athena é gerenciado e escala automaticamente para lidar com grandes volumes de dados e cargas de trabalho de 
consulta variáveis.

## Passo-a-passo:

1) Primeiramente, vamos criar uma função IAM (Identity and Access Management -IAM), para que o Glue possa executar funções na nuvem durante sua execução.<br>

* Na plataforma da AWS, busque pelo serviço IAM. Será aberto um painel. Selecione a opção "Gerenciamento de acesso" > "Funções" > "Criar Perfil".
* Será aberto um menu, com alguma opções. Selecione "Serviços da AWS" > "Casos de uso" > "Glue" > "Próximo".
* Será aberta uma página com vários roles para serem selecionadas. Vamos selecionar "AdministratorAccess" > "Próximo".

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/db0fbf0e-71a0-4101-9847-efba5fe4da61' height='250'/>
<div/><br>

* Nomeie sua função e selecione a opção de criar perfil.

2) Nesta etapa, vamos criar o bucket e as pastas que recerão os arquivos referentes ao projeto.
* Na AWS, busque pelo serviço S3 > "Criar Bucket".
* Nomeie seu bicket, selecione a região e selecione a opção "Criar".
* Agora vamos criar 5 pastas a primeira para receber os arquivos transformados, e as demais os logs, dados temporários, scripts e para os dados originários.<br>
<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/6b63474f-ff15-4654-a684-fa124123bc59' height='250'/>
<div/><br>
* Faça os upload dos [arquivos do projeto](https://github.com/micvet/curso-eng-dados-fa/tree/main/etl-data-crawler-glue-athena/files) na pasta destinada a receber os dados originários (a pasta foi nomeada como "Source").
<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/3e004293-ff4d-46a6-83d9-53cab8cefc1a' height='250'/>
<div/><br>

3) Com a estrutura criada, vamos iniciar o projeto com o Glue. Na barra de busca, busque pelo serviço Glue, 









