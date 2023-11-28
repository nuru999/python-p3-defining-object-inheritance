from vehicle import Vehicle

class Car(Vehicle):
        def go(self):
         return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
c = Car(1,23)
print(c.go())