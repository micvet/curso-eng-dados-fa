# NoSQL Chave-Valor com Redis e EC2 <br>

Neste módulo, aprendemos sobre o banco de dados NoSQL chave-valor Redis. Foi utilizada uma instância criada no EC2, da Azure, para instalar o banco de dados. Posteriormente, foi criado um código simples em Python para implementar e testar o Redis.

### Fluxograma: <br>

![image](https://github.com/micvet/curso-eng-dados-fa/assets/86981990/2b01197e-6381-4de5-92f3-919f97fc52be)



## Links Úteis

- [Python](https://www.python.org/)
- [Documentação do redis-py](https://redis-py.readthedocs.io/)

### Passo a passo:

1) Criação da instância EC2 na AWS:<br>
* Acesse a plataforma AWS, busque pelo serviço EC2 e selecione a opção de criar uma nova instância.  

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

2) Após a instância subir,  vamos nos conectar pelo terminal, via SSH. Para isso, no EC2, ao selecionar a opção de se conectar à instância, é possível selecionar algumas opções. Selecione "Cliente SSH" para verificar os parâmetros necessários. 

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/ff820482-3244-4601-93da-58c1bc5d495c' height='350'/>
<div/><br> 

* O exemplo fornecido (na parte inferior da opção de conectar-se àinstância) já deve funcionar. Basta executar o terminal, acessar o diretório em que se encontra a chave e executar o comando.<br>

<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/fa86218c-4d6e-46d6-bcd0-7158788f72db' height='350'/>
<div/><br> 

3) Após acessar o terminal, realize as instalações necessárias:
   * Para instalar o Redis:
     * sudo snap install redis
     * sudo apt-get update
     * sudo apt install redis-tools<br>

   * Verifique se o Python está instalado (é necessário que o programa esteja devidamnte instalado):
     *python3 --version
     
   * Instalar a biblioteca do Redis no Python:
     * pip install redis

4) Crie o arquivo com o script:
   * nano controle_tarefas.py
   * Copie e cole o código abaixo:
     * [Script](https://github.com/micvet/curso-eng-dados-fa/blob/main/redis-ec2/scripts/controle_tarefas.py)
     * Salve o arquivo
     * Para executá-lo, basta digitar o comando python3 controle_tarefas.py
    
5) Funcionamento do programa:
   * O programa se inicia com a importação da biblioteca redis, com a qual realizaremos a conexão e operações necessárias. Exitem quatro funções, com o objetivo de incluir uma nova tarefa, visualizar as tarefas já inclusas e deletar tarefas anteriores.
   * As funções são baseadas no armazenamento de strings, uma vez que os dados inseridos são estruturas simples.
  
<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/24644c51-2325-4fe4-9469-7b34e8895960' height='350'/>
<div/><br>

   * Na primeira função, os parâmetros incluem a conexão com o Redis e o valor que será inserido na descrição da tarefa. O id da tarefa será definido de forma incremental.
   * Por fim, na função Main, é criado um menu interativo, onde após selecionar a opção desejada e preencher os dados solicitados, os dados de entrada serão utilizados como parâmetro ao chamar a respectiva função.
   * Todos os dados criados são inseridos no banco de dados Redis local.

6) Verificando os dados inseridos por meio do programa, diretamente no Redis:
   * Acesse o Redis:
     * redis-cli
     * get tarefa:1
     * get tarefa:2
       
<div align='left'>
   <img src='https://github.com/micvet/curso-eng-dados-fa/assets/86981990/ca5e09b9-98d5-4384-bc88-fd37682622b4' height='100'/>
<div/><br>

  7) [Alguns comandos úteis](https://github.com/micvet/curso-eng-dados-fa/blob/main/redis-ec2/scripts/comandos_uteis.txt) :smile:
  
   
 

     
        



