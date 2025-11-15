class ShoppingCart:
    """
    Simple shopping cart to add/remove items
    and calculate totals.
    """

    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def remove(self, product_id):
        self.items = [p for p in self.items if p.id != product_id]

    def total_price(self):
        return sum(p.get_price() for p in self.items)

    def total_weight(self):
        return sum(p.get_weight() for p in self.items)
