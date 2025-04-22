from vehicle import Vehicle

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

vehicles = Boat(), 
for v in vehicles:
    print(v.move())
