from vehicle import Vehicle

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

vehicles = Car()
for v in vehicles:
    print(v.move())
