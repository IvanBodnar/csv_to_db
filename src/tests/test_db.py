from db.connect import ConnectDb


def test_connection():
    """
    Testea si hay conexión.
    """
    conn = ConnectDb('load_csv', 'ivan')
    conn._connect()
    assert conn._is_connected() == 0


def test_query():
    conn = ConnectDb('load_csv', 'ivan')
    q = conn.execute_query('select 1')
    assert q[0][0] == 1
