E-Commerce Product System
Create a Product class for a small e-commerce application.
Every product should have product ID, name, price, category, and stock quantity. Implement methods such as display_product(), update_stock() and calculate_total_price(quantity).
Create a static method
Product.is_valid_price(price)
It should return True if the price is greater than zero and False otherwise.
Create at least 5 different products and demonstrate buying/updating stock.

Sample Input:
p1 = Product(1, "Mobile", 10000, "Gadgets", 5)
p2 = Product(2, "Tablet", 30000, "Gadgets", 4)
p3 = Product(3, "Laptop", 50000, "Gadgets", 2)
p4 = Product(4, "Mouse", 500, "Gadgets", 20)
p5 = Product(5, "Keyboard", 1000, "Gadgets", 10)

Sample Output:
Product Details: 
Product ID: 1
Product Name: Mobile
Price: 10000
Category: Gadgets
Stock Quantity: 5
True
Added 2 Mobile(s) to cart. Remaining stock: 3
Product Details: 
Product ID: 2
Product Name: Tablet
Price: 30000
Category: Gadgets
Stock Quantity: 4
True
Added 1 Tablet(s) to cart. Remaining stock: 3
Product Details: 
Product ID: 3
Product Name: Laptop
Price: 50000
Category: Gadgets
Stock Quantity: 2
True
Added 1 Laptop(s) to cart. Remaining stock: 1
Product Details: 
Product ID: 4
Product Name: Mouse
Price: 500
Category: Gadgets
Stock Quantity: 20
True
Added 3 Mouse(s) to cart. Remaining stock: 17
Product Details: 
Product ID: 5
Product Name: Keyboard
Price: 1000
Category: Gadgets
Stock Quantity: 10
True
Not enough stock available!
Total Cart value is 101500
