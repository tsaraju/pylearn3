class Vehicle:
    def __init__(self, vehicleno, brand, model, rentperday):
        self.vehicleno = vehicleno
        self.brand = brand
        self.model = model
        self.rentperday = rentperday

    def calculate_rent(self, days):
        """Calculate rent for given days after validation."""
        if Vehicle.validate_days(days):
            total = days * self.rentperday
            print(f"{self.brand} {self.model} ({self.vehicleno})")
            print(f"Rent per day: {self.rentperday}, Days: {days}, Total Rent: {total}\n")
        else:
            print(f"Invalid number of days: {days}\n")

    @staticmethod
    def validate_days(days):
        """Static method to validate rental duration."""
        return days > 0

class Car(Vehicle):
    def __init__(self, vehicleno, brand, model, rentperday, seats):
        super().__init__(vehicleno, brand, model, rentperday)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, vehicleno, brand, model, rentperday, engine_capacity):
        super().__init__(vehicleno, brand, model, rentperday)
        self.engine_capacity = engine_capacity

# Demonstration
c1 = Car('KA12NS7589', 'Toyota', 'Fortuner', 5000, 7)
c1.calculate_rent(5)

c2 = Car('KA14NS8560', 'Maruti Suzuki', 'Jimny', 4000, 4)
c2.calculate_rent(3)

b1 = Bike('KA16NS5556', 'Suzuki', 'Gixxer', 2000, '250CC')
b1.calculate_rent(10)

b2 = Bike('KA16NS5557', 'Bajaj', 'Pulsar', 1800, '220CC')
b2.calculate_rent(8)