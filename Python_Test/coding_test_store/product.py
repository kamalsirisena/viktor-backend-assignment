class Product:
    """
    Base product class.
    All items in the store share an ID and price.
    """

    def __init__(self, product_id, price):
        self.id = product_id
        self.price = float(price)

    def get_price(self):
        return self.price

    def get_weight(self):
        """
        Software licenses do not have weight.
        Subclasses that support weight will override this.
        """
        return 0.0
