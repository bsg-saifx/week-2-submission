class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def details(self):
        print(f"Brand : {self.brand}\nModel: {self.model}")
    def price(self):
        pass

class Car(Vehicle):
    def price(self,price):
        self.price=price
        super().details()
        print(f"Price: {self.price} usd")
        
class Bike(Vehicle):
    def price(self,price):
        self.price=price
        super().details()
        print(f"Price: {self.price} usd")

if __name__ == "__main__":
    car = Car("Toyota","Supra Mk IV")
    price = car.price(150000)
    Bike = Bike("Kawasaki","Ninja H2R")
    price = Bike.price(30000)

