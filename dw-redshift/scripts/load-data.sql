COPY clientes -- tabela destino dos dados - altere conforme necessário
from 's3://mybucketcursode/dados/clientes.csv' --URI do arquivo do seu bucket para ser copiado para o banco -altere conforme necessário
credentials 'aws_access_key_id=SUA-CHAVE-DE-ACESSO;aws_secret_access_key=SUA-CHAVE-DE-ACESSO-SECRETA' --utilize esse formato, substituindo pela sua chave de acesso e chave de acesso secreta
region 'sa-east-1' -- Código da região do seu bucket
delimiter ';' --delimitador de dados do arquivo
IGNOREHEADER 1 --ignorar cabeçalho
DATEFORMAT 'DD/MM/YYYY';  -- formato da data
