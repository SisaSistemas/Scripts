import pyodbc
import os
'''
This archive is for exect Querys to automation process on SisaBD
'''

def query(query:str):
    '''
    we obtain the conection to SQL Server with and execute a query
    '''
    try:
        server = "187.251.105.179"
        database = "SisaAdmin-Copia"
        username = "sudo"
        password = "Sisa.2025_"
        driver = "ODBC Driver 17 for SQL Server"
        port = "1433"

        conection = pyodbc.connect(f"DRIVER={{{driver}}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}")
        cursor = conection.cursor() 
        cursor.execute(f'{query}') # execute the query

        if query.strip().lower().startswith("select"):
            for row in cursor:
                print(row)
        else:
            conection.commit()
        cursor.close()
        conection.close()
    except Exception as e:
        print(e)