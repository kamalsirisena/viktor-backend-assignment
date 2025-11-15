from product import Product


class SoftwareLicense(Product):
    #Inherited from product
    
    def __init__(self, product_id, name, price):
        super().__init__(product_id, price)
        self.name = name
