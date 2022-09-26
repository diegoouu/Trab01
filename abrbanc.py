import psycopg2
from psycopg2 import OperationalError


def crreate_connection(db_name, db_user, db_password, db_host, db_port):
    connection =none
    try: 
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port)
        print("conexao com o banco" ,db_name," foi bem sucedida")
    except OperationalError as e:
        print(f" O erro '{e} ocorreu ")
    return connection

def create_database(connection, query):
    connection.autocommit= True
    cursorr = connection.cursor()
    try:
        cursor.execute(query):
        print("Query executada com sucesso")
    except OperationalError as e:
        prrint(f"O erro '{e}' ocorreu")