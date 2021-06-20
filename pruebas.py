import argparse
import re
import sqlite3

'''
llista_preus = [
'$17.99',
'$3.49',
'$14.99',
'$8.49',
'$39.99'
]

for preu in llista_preus:
    currency = (re.sub('[0-9]', '', preu)).replace('.','')
    print(preu, currency)

#cambio local   
'''


parser = argparse.ArgumentParser()
parser.add_argument("Action")
args = parser.parse_args()

DDBB = 'Results.db'

if args.Action == 'Delete_Results' or args.Action == 'SetUp_Database':

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


if args.Action == 'See_Results':
    print('Se van a ver los resultados')

