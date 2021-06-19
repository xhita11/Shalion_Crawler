import scrapy
import json

class Target_Spider(scrapy.Spider):
    name = 'products'

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/'
        ]
    
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        print('Parsing')
        page = response.url.split("/")[-2]
        filename = f'quotes_products-{page}.html'
        print(response.body[:1000])
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


class Target_Spider_JSON(scrapy.Spider):
    name = 'products_JSON'

    '''
    url_1 = 'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&channel=WEB&count=24&default_purchasability_filter=true&include_sponsored=true&keyword='
    url_2 = '&offset=0&page=%2Fs%2Fice+cream+cones&platform=desktop&pricing_store_id=2159&store_ids=2159%2C2351%2C1215%2C1325%2C2016&useragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F91.0.4472.106+Safari%2F537.36&visitor_id=017A1AB8B0D10201AC07A3173C54DD11'

    product = 'ice cream cones'
    product.replace(' ','+')

    url = url_1 + product + url_2
    '''

    def start_requests(self):

        file = getattr(self, 'file', None)
        print(file)

        urls = [
            'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&channel=WEB&count=24&default_purchasability_filter=true&include_sponsored=true&keyword=ice+cream+cones&offset=0&page=%2Fs%2Fice+cream+cones&platform=desktop&pricing_store_id=2159&store_ids=2159%2C2351%2C1215%2C1325%2C2016&useragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F91.0.4472.106+Safari%2F537.36&visitor_id=017A1AB8B0D10201AC07A3173C54DD11'
        ]
    
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):


        jsonresponse = json.loads(response.body)
        
        for result in jsonresponse['data']['search']['products']:
            print(result['item']['merchandise_classification'])


        #print(jsonresponse)

        
        print('Parsing')
        page = response.url.split("/")[-2]
        filename = f'json_products-Ice_Cream.json'
        #print(jsonresponse[:1000])
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(jsonresponse, f, ensure_ascii=False, indent=4)
        #with open(filename, 'w') as f:
        #    json.dump(jsonresponse, f)
        self.log(f'Saved file {filename}')