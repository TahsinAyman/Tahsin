from lib.Human import Human


class Employee(Human):
    id = 0
    salary = 0
    bonus = 0

    def __init__(self, id, salary, bonus, name, age, religion, height, weight, gender):
        super().__init__(name, age, religion, height, weight, gender)
        self.id = id
        self.salary = salary
        self.bonus = bonus

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_bonus(self, bonus):
        self.bonus = bonus

    def get_bonus(self):
        return self.bonus

    def info(self):
        return super(Human.info()) + "\n[ID: " + self.id + "]\n[Salary: " + self.salary + "]\n[Bonus: " + self.bonus + "]\n"

