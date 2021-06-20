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

    if args.Accion == 'Delete_Results' :
        print('Se han eliminado los datos de la tabla Resultados')
    else:
        print('Se ha configurado la base de datos. "./Results.db"')


elif args.Accion == 'Show_Results':

    pd.set_option('display.max_columns', None)

    con = sqlite3.connect(DDBB)    # sqlite3
    cur = con.cursor()

    df_keywords = pd.read_sql_query("SELECT keyword, count(*) from Results group by keyword", con)
    print(df_keywords)  
    print('\n\n')

    df_results = pd.read_sql_query("SELECT keyword, title, price_amount, price_currency from Results order by keyword, id",con)
    print(df_results)
    con.close()

elif args.Accion == 'Export_Results':
    con = sqlite3.connect(DDBB)    # sqlite3
    cur = con.cursor()

    df_results = pd.read_sql_query("SELECT * from Results order by keyword, id",con)
    df_results.to_csv('./Results.csv')
    print('Results Exported to ./Results.csv')
    con.close()





    

















else:
    print(
'''
Accion no disponible. Introduzca una de las siguientes acciones por favor:
        - SetUp_Database
        - Delete_Results
        - Show_Results
''')