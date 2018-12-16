from core.database import *
from core.crawler import *

class Product:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        string = ''
        for k,v in vars(self).items():
            if k == 'img':
                string += k + '=' + str(v[:50]) + '...\n'
            else:
                string += k + '=' + str(v) + '\n'

        return string

    def save(self):
        db = Database()
        # db = Database(DBErrorHandler=DBExplodeOnError())

        # Create/Update the product record
        # db.query('insert into product (sku, name, img, description, price, size, alcohol, country, brewery) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update price=%s',
        db.query('insert into product (sku, name, img, description, price, size, alcohol, country, brewery) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (self.sku, self.name, b64decode(self.img), self.description, self.price, self.size, self.alcohol, self.country, self.brewery))

        db.query('select id from product where sku = %s limit 1', (self.sku))

        row = db.fetch_one()
        if row is None: return

        # Write the time-series record
        db.query('insert into product_data (product_id, price) values (%s,%s)',
            (row['id'], self.price))
