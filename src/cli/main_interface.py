import click
from cli.environment import (
    PGDATABASE, USER, PGHOST, PGPORT, PGPASSWORD
)
from db.connect import ConnectDb, execute_query
from db.queries import query_create_table, query_copy
from csv_process.extract import get_columns


@click.group()
@click.option('--db', default=PGDATABASE,
              help='Nombre de la Base de Datos. Default: variable PGDATABASE')
@click.option('--user', default=USER,
              help='Nombre de Usuario. Default: variable USER')
@click.option('--password', default=PGPASSWORD,
              help='Password de la Base de Datos. Default: PGPASSWORD')
@click.option('--host', default=PGHOST,
              help='Host de la Base de Datos. Default: PGHOST')
@click.option('--port', default=PGPORT,
              help='Port de la Base de Datos. Default: PGPORT')
@click.pass_context
def cl(ctx, db, user, password, host, port):
    connection = ConnectDb(db_name=db,
                           user=user,
                           password=password,
                           host=host,
                           port=port)
    # Pasa el objeto conexión al contexto
    ctx.obj['connection'] = connection.connect()


@cl.command()
@click.argument('file_path',
                type=click.Path(exists=True, resolve_path=True))
@click.argument('table_name', type=str)
@click.option('--schema_name', default='public',
              help='Esquema en el cual se desea crear la tabla. Default: public.')
@click.option('--encoding', default='utf8',
              help='Encoding en el que se encuentra el archivo. Para archivos en castellano'
                   ' es probable que deba usarse latin1. Default: utf8.')
@click.pass_context
def file(ctx, file_path, table_name, schema_name, encoding):
    # Toma la instancia de ConnectDb del contexto
    connection = ctx.obj['connection']
    cols = get_columns(file_path, encoding)
    execute_query(connection, query_create_table(schema_name, table_name, cols))
    execute_query(connection, query_copy(schema_name, table_name, file_path, ',', encoding))
    connection.close()





