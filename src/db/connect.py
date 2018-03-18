import psycopg2 as psy


class ConnectDb:
    def __init__(
            self,
            db_name,
            user,
            password=None,
            host=None,
            port=None
    ):
        self.conn_dict = {
            'dbname': db_name,
            'user': user
        }
        if password is not None:
            self.conn_dict['password'] = password
        if host is not None:
            self.conn_dict['host'] = host
        if port is not None:
            self.conn_dict['port'] = port

    def connect(self):
        try:
            conn = psy.connect(**self.conn_dict)
        except psy.OperationalError as e:
            print('Error de conexión: {}'.format(e))
            conn = None
        return conn


def execute_query(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query)
    except psy.ProgrammingError as e:
        print('Error: {}'.format(e))
    except psy.DatabaseError as e:
        print('Error: {}'.format(e))
    finally:
        conn.commit()
