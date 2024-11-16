import oracledb

# Função para conectar ao banco de dados
def conectar_banco():
    dsn = oracledb.makedsn("localhost", 1522, service_name="xe")
    connection = oracledb.connect(user="usr_studiolima", password="123456", dsn=dsn)
    return connection
