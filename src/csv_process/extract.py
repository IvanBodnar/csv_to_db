import csv


def _format_columns(columns):
    """
    Formatea las columnas para
    insertarlas en la query CREATE TABLE.
    :param columns: list de los nombres de las columnas
    :return: str
    """
    return ', '.join(col.strip().lower() + ' text' for col in columns)


def get_columns(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as f:
        reader = csv.reader(f)
        columns_list = list(reader)[0]
        return _format_columns(columns_list)


