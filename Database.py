import argparse
import sqlite3
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("Accion")
args = parser.parse_args()

DDBB = 'Results.db'

if args.Accion == 'Delete_Results' or args.Accion == 'SetUp_Database':

    con = sqlite3.connect(DDBB)    # sqlite3
    cur = con.cursor()

    try:
        cur.execute("DROP TABLE Results")
    except:
        pass

    sql = '''CREATE TABLE Results 
                (id INTEGER NOT NULL, 
                title TEXT, 
                url TEXT, 
                image_url TEXT,
                price_amount REAL, 
                price_currency TEXT, 
                _validation TEXT,
                keyword TEXT)'''

    #print (sql)
    cur.execute(sql)    
    con.close()

    print('Se han truncado la tabla de resultados')


elif args.Accion == 'Show_Results':



    print('Se van a ver los resultados')


else:
    print(
'''
Accion no disponible. Introduzca una de las siguientes acciones por favor:
        - SetUp_Database
        - Delete_Results
        - Show_Results
''')