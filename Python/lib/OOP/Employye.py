class Employee:
    id = int()
    salary = int()
    bonus = int()

    def __call__(self, *args, **kwargs):
        pass

    def __bytes__(self):
        print('Ok')

    def __init__(self, id, salary, bonus):
        self.id = id
        self.salary = salary
        self.bonus = bonus

    def __del__(self):
        pass

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

    def __str__(self):
        return f"[ID: {self.id}]\n[Salary: {self.salary}]\n[Bonus: {self.bonus}]\n"
