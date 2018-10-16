import uuid


class Product(object):
    def __init__(self,product_name,product_quantity,product_price,product_description):
        self.product_id = uuid.uuid1()
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_description = product_description

    def to_dict(self):
        return dict(
            product_id = str(uuid.uuid4().int)[:5],
            product_name = self.product_name,
            product_quantity = self.product_quantity,
            product_price = self.product_price,
            product_description = self.product_description
        )



