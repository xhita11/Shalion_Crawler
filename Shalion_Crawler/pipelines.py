# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
'''
from itemadapter import ItemAdapter


class ShalionCrawlerPipeline:
    def process_item(self, item, spider):
        return item

'''

import os
import sqlite3      # pip install pysqlite3
#import apsw        # pip install apsw

from scrapy import settings, signals
from scrapy.utils.project import get_project_settings
settings = get_project_settings() 
from Shalion_Crawler.items import ProductsItem     # Get items from "items.py"



import os
import sqlite3      # pip install pysqlite3
#import apsw        # pip install apsw


con = None
ikeys = None

class DbPipeline(object):
    dbfile  = settings.get('SQLITE_FILE')   # './test.db'
    dbtable = settings.get('SQLITE_TABLE')

    def __init__(self):
        self.setupDBCon()
        #self.createTables()

    def setupDBCon(self):
        #self.con = apsw.Connection(self.dbfile)   # apsw
        self.con = sqlite3.connect(self.dbfile)    # sqlite3
        self.cur = self.con.cursor()

    def createTables(self):

        self.dropDbTable()
        self.createDbTable()

    def dropDbTable(self):
        try:
            self.cur.execute("DROP TABLE Results")
        except:
            pass
        

    def closeDB(self):
        self.con.close()

    def __del__(self):
        self.closeDB()

    def createDbTable(self):
        #------------------------------
        # Construct the item strings:
        #------------------------------
        # NOTE: This does not work, because items.py class re-orders the items!
        #self.ikeys = NewAdsItem.fields.keys()
        #print("Keys in creatDbTable: \t%s" % ",".join(self.ikeys) )
        #cols = " TEXT, ".join(self.ikeys)  + " TEXT"
        #print("cols:  \t%s:" % cols, flush=True)
        #------------------------------

        # NOTE:  Use "INSERT OR IGNORE", if you also use: "AdId TEXT NOT NULL UNIQUE"
        sql = '''CREATE TABLE Results 
                    (id INTEGER PRIMARY KEY NOT NULL, 
                    title TEXT, 
                    url TEXT, 
                    image_url TEXT,
                    price_amount REAL, 
                    price_currency TEXT, 
                    _validation TEXT,
                    keyword TEXT)'''

        print('\n\nTABLA CREADAAAAA\n\n\n\n\n\n\n\n\n\n\n\n')

        #print (sql)
        self.cur.execute(sql)

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def storeInDb(self, item):
        # NOTE:  Use "INSERT OR IGNORE", if you also use: "AdId TEXT NOT NULL UNIQUE"
        # "INSERT INTO ads ( AdId, DateR, AdURL ) VALUES (?, ?, ?)"
        sql = f'''INSERT INTO Results VALUES (
                {item.get("id")}, 
                "{item.get("title")}", 
                "{item.get("url")}", 
                "{item.get("image_url")}", 
                {item.get("price_amount")}, 
                "{item.get("price_currency")}", 
                "{str(item.get("_validation"))}",
                "{item.get("keyword")}"
                )
                '''
                   #.format(self.dbtable, ','.join(item.keys()), ','.join(['?'] * len(item.keys())) )

        # (item.get('AdId',''),item.get('DateR',''),item.get('AdURL',''), ...)


        #print (sql)
        #print("  itkeys: \t%s" % itkeys, flush=True)
        #print("  itvals: \t%s" % itvals, flush=True)
        self.cur.execute(sql)     # WARNING: Does NOT handle '[]'s ==> use: '' in spider

        self.con.commit()               # used in sqlite3 ONLY! (Remove for APSW)