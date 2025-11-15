from product import Product



class Book(Product):
    #Inherited from Product
     
    def __init__(self, product_id, title, author, pages, price, weight):
        super().__init__(product_id, price)
        self.title = title
        self.author = author
        self.pages = int(pages)
        self.weight = float(weight)

    def get_weight(self):
        return self.weight
