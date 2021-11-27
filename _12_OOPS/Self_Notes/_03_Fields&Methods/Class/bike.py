#14. Creating class of a bike.

class Bike:
    
    def __init__(self, model, engine_type, power, torque, color, starter):
        self.model = model
        self.engine_type = engine_type
        self.power = power
        self.torque = torque
        self.color = color
        self.starter = starter

    def engine_specifications(self):
        print("Details of most expensive bike in the world: ", self.model, self.engine_type, self.power, self.torque, self.color, self.starter)

info = Bike("Ecosse Spirit ES1", "V4, four-stroke", "200.0 HP", "189.8 Nm", "Orange", "Electric")
info.engine_specifications()
