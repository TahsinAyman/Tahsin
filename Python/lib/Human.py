class Human:
    name = ""
    age = int()
    religion = ""
    height = float()
    weight = float()
    gender = ""

    def __init__(self, name, age, religion, height, weight, gender):
        self.name = name
        self.age = age
        self.religion = religion
        self.height = height
        self.weight = weight
        self.gender = gender

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_religion(self, religion):
        self.religion = religion

    def get_religion(self):
        return self.religion

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def info(self):
        return "\n[Name: " + self.name + "]\n[Religion: " + self.religion + "]\n[Gender: " + self.gender + "]\n[Age: " + self.age + "]\n[Height: " + self.height + "]\n[Weight: " + self.weight + "]\n"
