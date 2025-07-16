class Staff:
    def __init__(self, staff_id, name, basic_salary):
        self.staff_id = staff_id
        self.name = name
        self.basic_salary = basic_salary

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id
    
    def set_name(self, name):
        self.name = name
    
    def set_basic_salary(self, basic_salary):
        self.basic_salary = basic_salary

    def get_staff_id(self):
        return self.staff_id
    
    def get_name(self):
        return self.name
    
    def get_basic_salary(self):
        return self.basic_salary
    
    def calculate_salary(self):
        return self.basic_salary * 1.2
    
    def display(self):
        print("Staff ID: {}, Name: {}, Basic Salary: {:.2f}".format(self.staff_id, self.name, self.basic_salary))
    
    def __str__(self):
        return "Staff ID: {}, Name: {}, Basic Salary: {:.2f}".format(self.staff_id, self.name, self.basic_salary)


class Teacher(Staff):
    def __init__(self, staff_id, name, basic_salary, subject_allowance):
        super().__init__(staff_id, name, basic_salary)
        self.subject_allowance = subject_allowance
    
    def set_subject_allowance(self, subject_allowance):
        self.subject_allowance = subject_allowance

    def get_subject_allowance(self):
        return self.subject_allowance
    
    def calculate_salary(self):
        return super().calculate_salary() + self.subject_allowance
    
    def display(self):
        print("Staff ID: {}, Name: {}, Basic Salary: {:.2f}, Subject Allowance: {:.2f}".format(
            self.staff_id, self.name, self.basic_salary, self.subject_allowance))
    
    def __str__(self):
        return super().__str__() + ", Subject Allowance: {:.2f}".format(self.subject_allowance)


class Janitor(Staff):
    def __init__(self, staff_id, name, basic_salary, shift_hours, hourly_rate):
        super().__init__(staff_id, name, basic_salary)
        self.shift_hours = shift_hours
        self.hourly_rate = hourly_rate

    def set_shift_hours(self, shift_hours):
        self.shift_hours = shift_hours

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def get_shift_hours(self):
        return self.shift_hours

    def get_hourly_rate(self):
        return self.hourly_rate 

    def calculate_salary(self):
        return self.basic_salary * 1.2 + (self.shift_hours * self.hourly_rate)  
    
    def display(self):
        print("Staff ID: {}, Name: {}, Basic Salary: {:.2f}, Shift Hours: {}, Hourly Rate: {:.2f}".format(
            self.staff_id, self.name, self.basic_salary, self.shift_hours, self.hourly_rate))

    def __str__(self):
        return self.__str__() + ", Shift Hours:mn {}, Hourly Rate: {:.2f}".format(self.shift_hours, self.hourly_rate)


# ========================
# Testing the classes
# ========================
s = Staff(1, "John Doe", 3000)
s.display()
print("Salary:", s.calculate_salary())

t = Teacher(2, "Jane Smith", 3500, 500)
t.display()
print("Salary:", t.calculate_salary())

j = Janitor(3, "Jim Brown", 2500, 40, 15)
j.display()
print("Salary:", j.calculate_salary())

j.set_hourly_rate(20)
j.set_shift_hours(45)
j.display()
print("Updated Salary:", j.calculate_salary())
