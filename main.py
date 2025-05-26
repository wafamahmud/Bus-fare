class vehicle:
    def fare(self):
        return 50 * 100
    
class bus(vehicle):
    def fare(self):
        total = super().fare()
        return total + (total * 0.10) 

bus = bus()
print("Total bus fare : TK.", bus.fare())

