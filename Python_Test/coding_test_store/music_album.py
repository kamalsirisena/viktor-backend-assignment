from product import Product


class MusicAlbum(Product):
    #Inherited from product
    
    def __init__(self, product_id, artist, title, tracks, price, weight):
        super().__init__(product_id, price)
        self.artist = artist
        self.title = title
        self.tracks = int(tracks)
        self.weight = float(weight)

    def get_weight(self):
        return self.weight
