
def query_create_table(schema_name, table_name, columns):
    """
    Crea una tabla con el nombre y las
    columnas especificadas (todas type text).
    :param schema_name: str
    :param table_name: str
    :param columns: list
    :return:
    """
    q = """
        CREATE TABLE IF NOT EXISTS {}.{} ({});
    """.format(schema_name, table_name, columns)
    return q


def query_copy(schema_name, table_name, file, delimiter, encoding):
    q = """
        COPY {}.{} FROM '{}' DELIMITER '{}' CSV HEADER ENCODING '{}';
    """.format(schema_name, table_name, file, delimiter, encoding)
    return q
