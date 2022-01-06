class Employee:
    id = int()
    salary = int()
    bonus = int()

    def __int__(self):
        pass

    def __init__(self, id, salary, bonus):
        self.id = id
        self.salary = salary
        self.bonus = bonus

    def set_id(self, id):
        self.id = id

    def set_salary(self, salary):
        self.salary = salary

    def set_bonus(self, bonus):
        self.bonus = bonus

    def get_id(self):
        return self.id

    def get_salary(self):
        return self.salary

    def get_bonus(self):
        return self.bonus

    def toString(self):
        return f"[ID: {self.id}]\n[Salary: {self.salary}]\n[Bonus: {self.bonus}]\n"
