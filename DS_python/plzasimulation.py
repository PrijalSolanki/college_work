from collections import deque

class simulation:
    def __init__(self):
        self.vehicles = deque(maxlen=5)
    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)
        print(self.vehicles)
        if len(self.vehicles) == 5:
            print("Queue is full. Cannot add more vehicles.")
        elif len(self.vehicles) < 5:
            print("Queue is not full. You can add more vehicles.")

v= simulation()
v.add_vehicle("Car1")
v.add_vehicle("Car2")
v.add_vehicle("Car3")
v.add_vehicle("Car4")
v.add_vehicle("Car5")
v.add_vehicle("Car6")