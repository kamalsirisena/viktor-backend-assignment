from book import Book
from music_album import MusicAlbum
from software_license import SoftwareLicense
from shopping_cart import ShoppingCart
from recommendation import product_addition_order_stats


# Create some products
b1 = Book("B1", "Python 101", "John Smith", 300, 25, 0.7)
b2 = Book("B2", "Django Guide", "Anna Lee", 250, 22, 0.5)

a1 = MusicAlbum("A1", "Coldplay", "Parachutes", 10, 15, 0.2)

s1 = SoftwareLicense("S1", "Photoshop Pro", 299)

# Create carts
c1 = ShoppingCart()
c1.add(b1)
c1.add(a1)
c1.add(b2)

c2 = ShoppingCart()
c2.add(b1)
c2.add(a1)

c3 = ShoppingCart()
c3.add(a1)
c3.add(b2)

# Show totals
print("Cart 1 price:", c1.total_price())
print("Cart 1 weight:", c1.total_weight())

# Recommendation stats
stats = product_addition_order_stats([c1, c2, c3])
print(stats)
