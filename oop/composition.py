class Engine:

    def __init__(self, horse_power) -> None:
        self.horse_power = horse_power


class Wheels:

    def __init__(self, size) -> None:
        self.size = size


class Car:

    def __init__(self, make, model, wheel_size, horse_power) -> None:
        self.make = make
        self.model = model
        self.wheels = [Wheels(wheel_size) for i in range(4)]
        self.engine = Engine(horse_power)

    def get_details(self):
        return f"{self.model} {self.make} {self.wheels[0].size}in {self.engine.horse_power}cc"

chevrolet = Car("Chevrolet", "Mustang", 15, 670)
print(chevrolet.get_details())