import mariadb
import dbcreds

def connect_db():
  try:
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    return cursor
  except mariadb.OperationalError as error:
    print("OPERATIONAL ERROR:", error)
  except Exception as error:
    print("UNEXPECTED ERROR:", error) 

def execute_statement(cursor, statement, args = []):
    try:
        cursor.execute(statement, args)
        results = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        records = [dict(zip(column_names, row)) for row in results]
        return records
    except mariadb.ProgrammingError as error:
        print("PROGRAMMING ERROR:", error)
        return str(error)
    except mariadb.IntegrityError as error:
        print("INTEGRITY ERROR:", error)
        return str(error)
    except mariadb.DataError as error:
        print("DATA ERROR:", error)
        return str(error)
    except Exception as error:
        print("UNEXPECTED ERROR:", error)
        return str(error)       

def close_connection(cursor):
  try:
    conn = cursor.connection
    conn.close()
    cursor.close()
    print("Connection closed")
  except mariadb.OperationalError as error:
    print("OPERATIONAL ERROR:", error)
  except mariadb.InternalError as error:
    print("INTERNAL ERROR:", error)
  except Exception as error:
    print("UNEXPECTED ERROR:", error)

def run_statement(statement, list_of_args = []):
  cursor = connect_db()
  if (cursor == None):
    return "Connection Error"
  results = execute_statement(cursor, statement, list_of_args)
  if(results == None):
    return "Statement Error"
  close_connection(cursor)
  return results
