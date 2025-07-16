from address import Address

class Employee:
    def __init__(self, id, name, dept_id, basic_salary, address):
        self.id = id
        self.name = name
        self.dept_id = dept_id
        self.basic_salary = basic_salary
        self.address = address

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_dept_id(self, dept_id):
        self.dept_id = dept_id

    def set_address(self, address):
        self.address = address

    def set_basic_salary(self, basic_salary):
        self.basic_salary = basic_salary

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dept_id(self):
        return self.dept_id

    def get_address(self):
        return self.address

    def get_basic_salary(self):
        return self.basic_salary

    def calculate_salary(self):
        return self.basic * 1.5

    def __str__(self):
        return 'ID: {}, Name: {}, Dept ID: {}, Basic: {:.2f}, Address: {}'.format(
            self.id, self.name, self.dept_id, self.basic_salary, self.address
        )

    def display(self):
        print(self.__str__())
