# weather

#Funcionalidade#

Serviço para retorno da previsão do tempo a partir dos dados coletados da API OpenWether

Endpoint GET
localhost:6000/weather?city='Blumenau'

Historicos de consulta por cidade:
Endpoint GET
localhost:6000/history?city='Blumenau'

Caso utilizado a ferramenta Postman, basta impotar o arquivo "OpenWeather.postman_collection.json" para realizar as consultas

#Dependencias instalação#

Python 3.7,
PostgreSQL 9.1,
Postman (Opcional)

#Dependencias Python#

flask
psycopg2

#Passo a passo#

-Instalar as dependencias
- (DBeaver) Criar banco de dados PostgreSQL e executar script "createTables.SQL" para criação das tabelas necessarias e seus relacionamentos
- Alterar variaveis de conexão no arquivo "connectdb.py conforme a configuração do banco
- Alterar variavel myKey do arquivo "openWeather.py" conforme key do cadastro do OpenWeather (Opcional)
- (Anaconda) Criar e iniciar ambiente virtual python
- No ambiente virtual, acessar a pasta principal da aplicação e executar o comando "python openWeather.py"
- (Postman) Realizar pesquisas por nome de cidades pelo método GET na rota localhost:6000/weather?city='Blumenau'
-- Ao realizar a pesquisa pelo endpoint /weather o sistema grava no banco de dados a cidade e o resultado retornado pela pesquisa
- (Postman) Realizar a pesquisa de historicos de consulta pelo método GET na rota localhost:6000/history?city='Blumenau'
