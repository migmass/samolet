class Vehicle:
    def __new__(cls, *args, **Kwargs):
        vechicle_type= args[0]
        if vechicle_type == "car":
            return super(Vehicle, cls).__new__(Car)
        elif vechicle_type =="bike":
            return super(Vehicle, cls).__new__(Bike)
        else:
            return None
        
class Car(Vehicle):
    def drive(self):
        return "Driving a car"
    
class Bike(Vehicle):
    def ride(self):
        return "Riding a bike"
    
# Создание разных объектов с помощью __new__

vehicle1=Vehicle("car")
vehicle2=Vehicle("bike")

print(vehicle1.drive())
print(vehicle2.ride())