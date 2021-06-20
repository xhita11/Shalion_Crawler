from Shalion_Crawler.items import ProductsItem
import scrapy
import json
import logging
import re


class Products(scrapy.Spider):
    name = "products_spider"

    def start_requests(self):
        

        url_1 = 'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&channel=WEB&count=24&default_purchasability_filter=true&include_sponsored=true&keyword='
        url_2 = '&offset=0&page=%2Fs%2Fice+cream+cones&platform=desktop&pricing_store_id=2159&store_ids=2159%2C2351%2C1215%2C1325%2C2016&useragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F91.0.4472.106+Safari%2F537.36&visitor_id=017A1AB8B0D10201AC07A3173C54DD11'
        
        json_file = getattr(self, 'json_input', None)

        f = open(json_file)
  
        url_dic = {}

        data = json.load(f)
        for product in data['keywords']:
            url_dic[product] = url_1 + product.replace(' ','+') + url_2

            
        for product in url_dic:
            yield scrapy.Request(url=url_dic[product], callback=self.parse_product, meta={'Product':product})
        



    def parse_product(self, response):

        jsonresponse = json.loads(response.body)
        results = []    
        for result in jsonresponse['data']['search']['products']:
            
            id =  result['tcin']
            
            title = result['item']['product_description']['title']
            url = result['item']['enrichment']['buy_url']
            image_url = result['item']['enrichment']['images']['primary_image_url']
            price_amount = float(result['price']['current_retail'])
            
            price_currency = result['price']['formatted_current_price']
            price_currency = (re.sub('[0-9]', '', price_currency)).replace('.','')

            # if '$' in price_currency:
            #     price_currency = 'USD'
            # elif '€' in price_currency:
            #     price_currency = 'EUR'
            
            
            product = ProductsItem(
                title = title,
                id = id,
                url = url,
                image_url = image_url,
                price_amount = price_amount,
                price_currency = price_currency,
                keyword = response.meta['Product']
            )

            yield product

        

        