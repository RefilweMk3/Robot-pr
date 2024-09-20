
class robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose
    def intro(self):
        return f"Hello, I am {self.name}, A {self.model} robot designed for {self.purpose}."

class SR(robot):
    def __init__(self, name, model, purpose, service_area):
        super().__init__(name, model, purpose)
        self.service_area = service_area
    def intro(self):
        return f"Hello there I'm {self.name}, An {self.model} robot. I work in {self.service_area} for {self.purpose}."
class IR(robot):
    def __init__(self, name, model, purpose, production_line):
        super().__init__(name, model, purpose)
        self.production_line = production_line
    def intro(self):
        return f"Greetings, I am {self.name}, An {self.model} robot, and I operate on the {self.production_line} production line for {self.purpose}."

robot1 = robot("Robo1", "Basic", "general assistance")
robot2 = SR("ServBot", "SR-200", "customer service", "hospitality")
robot3 = IR("InduBot", "IR-500", "assembling products", "automobile")

print(robot1.intro())
print(robot2.intro())
print(robot3.intro())