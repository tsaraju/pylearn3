class Product:
    prods = 0
    cart = {}

    def __init__(self, prodId, pname, price, category, stock_quantity):
        self.prodId = prodId
        self.pname = pname
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity
        Product.prods += 1

    def display_product(self):
        print("Product Details: ")
        print(f"Product ID: {self.prodId}")
        print(f"Product Name: {self.pname}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")
        print(f"Stock Quantity: {self.stock_quantity}")

    def update_stock(self, quantity):
        if quantity <= self.stock_quantity:
            Product.cart[self.pname] = self.calculate_total_price(quantity)
            self.stock_quantity -= quantity
            print(f"Added {quantity} {self.pname}(s) to cart. Remaining stock: {self.stock_quantity}")
        else:
            print("Not enough stock available!")

    def calculate_total_price(self, quantity):
        return self.price * quantity

    @staticmethod
    def is_valid_price(price):
        return price > 0


# Demo
p1 = Product(1, "Mobile", 10000, "Gadgets", 5)
p2 = Product(2, "Tablet", 30000, "Gadgets", 4)
p3 = Product(3, "Laptop", 50000, "Gadgets", 2)
p4 = Product(4, "Mouse", 500, "Gadgets", 20)
p5 = Product(5, "Keyboard", 1000, "Gadgets", 10)

p1.display_product()
print(Product.is_valid_price(p1.price))
p1.update_stock(2)

p2.display_product()
print(Product.is_valid_price(p2.price))
p2.update_stock(1)

p3.display_product()
print(Product.is_valid_price(p3.price))
p3.update_stock(1)

p4.display_product()
print(Product.is_valid_price(p4.price))
p4.update_stock(3)

p5.display_product()
print(Product.is_valid_price(p5.price))
p5.update_stock(15)

print(f"Total Cart value is {sum(Product.cart.values())}")