from vehicle import Vehicle

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

vehicles = Plane()
for v in vehicles:
    print(v.move())
