
class Car:
    def __init__(self, make, model, fuel_level):
        self.make = make
        self.model = model
        self._fuel_level = fuel_level

    def refuel(self, amount):
        self._fuel_level += amount
        return self._fuel_level

    def get_fuel_level(self):
        print(f"Current level: {self._fuel_level}")


class electric_car(Car):
    def __init__(self,  battery_level):
        super().__init__(make, model, fuel_level)
        self.__battery_level = battery_level

    def charge(self, amount):
        self.__battery_level += amount
        return self.__battery_level

    @classmethod
    def from_string(cls, car_str, fuel_level, battery_level):
        make, model = car_str.split("-")
        return cls(make, model, fuel_level, battery_level)

e1 = electric_car .from_string("Tesla-Model3", 10, 80)
e1.get_fuel_level()     
print(e1.charge(20))
e1.refuel(15)
e1.get_fuel_level()

