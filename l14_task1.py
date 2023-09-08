class Product(object):
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty


class Book(Product):
    def __init__(self, name, price, qty, author):
        super().__init__(name, price, qty)
        self.author = author

    def read(self):
        return f'Book: {self.name}; price: {self.price}; ' \
            f'Quantity: {self.qty}; author: {self.author}'


harry_potter = Book('Harry Potter', 400, 10, 'J.K. Rowling')

print(harry_potter.read())
