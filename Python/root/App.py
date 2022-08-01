class Father:
    car = None
    house = None

    def __init__(car: str, house: str, self):
        self.car, self.house = car, house

    def sleep(self):
        return "Father Sleeping"

class Mother:
    stiching = None

    def __init__(self, stiching):
        self.stiching = stiching

    def sleep(self):
        return "Mother Sleeping"


class Child(Mother, Father):

    def __init__(self, car, house, stiching):
        self.car = car
        self.house = house
        self.stiching = stiching


child = Child("Lambo", "Bari", "Stiching")
print(child.Mother.sleep())
