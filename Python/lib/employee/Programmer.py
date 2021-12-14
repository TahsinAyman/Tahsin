from lib.employee.Employee import Employee


class Programmer(Employee):
    work_description = ''''''

    def __init__(self, work_description, id, salary, bonus, name, age, religion, height, weight, gender):
        super().__init__(id, salary, bonus, name, age, religion, height, weight, gender)
        self.work_description = work_description

    def set_work_description(self, work_description):
        self.work_description = work_description

    def get_work_description(self):
        return self.work_description

    def info(self):
        return "[Work Description: \n" + self.work_description + "]\n"
