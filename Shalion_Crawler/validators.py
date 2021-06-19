from schematics.models import Model
from schematics.types import URLType, StringType, IntType, DecimalType
from ISO_Rule import ISO_4217

class ProductItem(Model):
    
    id = IntType(required=True)
    title = StringType(required=True)
    url = URLType(required=True)
    image_url = URLType(required=True)
    price_amount = DecimalType(required=True)
    price_currency = ISO_4217(required=True)
    keyword = StringType(required=True)