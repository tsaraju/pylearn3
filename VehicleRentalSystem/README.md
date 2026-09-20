Vehicle Rental System
Build a mini vehicle rental application.

Create a parent Vehicle class containing vehicle number, brand, model, and rental price per day.
Then create
Vehicle
|
+---- Car
|
+---- Bike

Car can have an additional attribute such as number of seats, while Bike can have engine capacity.
Create a method
calculate_rent(days)
Also create a static method that validates whether the rental duration is valid—for example, the number of rental days must be greater than zero.
Create at least 2 cars and 2 bikes and demonstrate the complete system.

Sample Input: 
c1 = Car('KA12NS7589', 'Toyota', 'Fortuner', 5000, 7)
c1.calculate_rent(5)

c2 = Car('KA14NS8560', 'Maruti Suzuki', 'Jimny', 4000, 4)
c2.calculate_rent(3)

b1 = Bike('KA16NS5556', 'Suzuki', 'Gixxer', 2000, '250CC')
b1.calculate_rent(10)

b2 = Bike('KA16NS5557', 'Bajaj', 'Pulsar', 1800, '220CC')
b2.calculate_rent(8)

Sample Output:
Toyota Fortuner (KA12NS7589)
Rent per day: 5000, Days: 5, Total Rent: 25000

Maruti Suzuki Jimny (KA14NS8560)
Rent per day: 4000, Days: 3, Total Rent: 12000

Suzuki Gixxer (KA16NS5556)
Rent per day: 2000, Days: 10, Total Rent: 20000

Bajaj Pulsar (KA16NS5557)
Rent per day: 1800, Days: 8, Total Rent: 14400
