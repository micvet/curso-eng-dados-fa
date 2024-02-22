# ETL e Data Crawler com Glue e Athena<br>

Neste módulo, 

**Após o uso todos os recursos utilizados na plataforma AWS foram excluídos, por tanto, os acessos que podem estar presentes nas imagens não funcionarão**<br>
## Fluxograma:


### Sobre as aplicações utilizadas: 
* AWS Glue: é um serviço de ETL (Extract, Transform, Load) gerenciado que facilita a preparação e o carregamento de dados para análise. 
Fornece recursos para descobrir, catalogar, limpar e transformar dados.
Principais funcionalidades: 

    * Armazenamento de metadados: O Glue possui um catálogo de dados centralizado que armazena metadados sobre os dados processados. 
Isso inclui informações sobre a estrutura dos dados, esquemas, dependências e estatísticas. O catálogo de dados permite a descoberta e exploração de 
conjuntos de dados e rastreio da origem e do histórico de transformações.

    * ETL Gerenciado: Permite a criação de fluxos de trabalho de ETL sem provisionar ou gerenciar infraestrutura. 
Pode-se definir transformações usando uma interface visual ou escrevendo códigos. O Glue executa automaticamente os fluxos de trabalho, 
dimensionando a infraestrutura conforme necessário.

    * Integração com Outros Serviços da AWS: O Glue integra-se com outros serviços da AWS, como S3, Redshift, RDS, Athena e EMR. 

    * Descoberta e Catalogação Automática: O Glue pode descobrir automaticamente a estrutura e o esquema dos seus dados e catalogá-los no catálogo de dados.

* Athena: Amazon Athena é um serviço de análise interativa da AWS que permite consultar dados diretamente no Amazon S3 usando SQL padrão. Não é necessário
configurar ou gerenciar infraestrutura, e pode-se executar consultas ad hoc em grandes volumes de dados armazenados no S3 sem a necessidade de carregar os dados
em um armazenamento de dados tradicional. Principais funcionalidades:

  * Consultas SQL Padrão: suporta consultas SQL padrão, permitindo a escrita de consultas para analisar dados. 

  *  Integração com o Amazon S3: é integrado diretamente com o Amazon S3, permitindo a consulta de dados armazenados em qualquer formato suportado pelo S3.

  * Escalabilidade Automática: O Athena é gerenciado e escala automaticamente para lidar com grandes volumes de dados e cargas de trabalho de 
consulta variáveis.


