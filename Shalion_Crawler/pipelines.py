# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


from scrapy import settings, signals
from scrapy.utils.project import get_project_settings
settings = get_project_settings() 
from Shalion_Crawler.items import ProductsItem     # Get items from "items.py"

import os
import sqlite3      



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
        self.con.commit()
        self.closeDB()

    def createDbTable(self):

        sql = '''CREATE TABLE Results 
                    (id INTEGER PRIMARY KEY NOT NULL, 
                    title TEXT, 
                    url TEXT, 
                    image_url TEXT,
                    price_amount REAL, 
                    price_currency TEXT, 
                    _validation TEXT,
                    keyword TEXT)'''



        self.cur.execute(sql)
        

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def storeInDb(self, item):
        
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
                   

        self.cur.execute(sql)     # WARNING: Does NOT handle '[]'s ==> use: '' in spider
        