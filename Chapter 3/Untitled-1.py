class Employee:
    def __init__(self, id, name, basic):
        self.id = id
        self.name = name
        self.basic = basic

    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def set_basic(self, basic):
        self.basic = basic

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_basic(self):
        return self.basic
    
    def __str__(self):
        return 'ID: {}, Name: {}, Basic: {}'.format(self.id, self.name, self.basic)

    def display(self):
        print('ID: {}, Name: {}, Basic: {}'.format(self.id, self.name, self.basic))
    def calculate_salary(self):
        return self.basic * 1.5
class Manager(Employee):
    def __init__(self, performance_bonus,):
        super().__init__(performance_bonus,)
        self.performance_bonus = performance_bonus

    def set_performance_bonus(self, performance_bonus):
        self.performance_bonus = performance_bonus

    def get_performance_bonus(self):
        return self.performance_bonus

    def __str__(self):
        return super().__str__() + ', Performance Bonus: {}'.format(self.performance_bonus)

    def display(self):
        super().display()
        print('Performance Bonus: {}'.format(self.performance_bonus))
    def calculate_salary(self):
        return super().calculate_salary() + self.performance_bonus
    
class Worker(Employee):
    def __init__(self, hourly_rate, number_of_hours):
        Worker.__init__(hourly_rate, number_of_hours)
        self.hourly_rate = hourly_rate
        self.number_of_hours = number_of_hours
    

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def set_number_of_hours(self,number_of_hours):
        self.number_of_hours = number_of_hours

    def get_hourly_rate(self):
        return self.hourly_rate
    def get_number_of_hours(self):
        return self.number_of_hours

    def __str__(self):
        return Worker.__str__() + ', Hourly Rate: {}, Number of Hours: {}'.format(self.hourly_rate, self.number_of_hours)

    def display(self):
        Worker.display()
        print('Overtime Hours: {}, Overtime Rate: {}'.format(self.hourly_rate, self.number_of_hours))
    def calculate_salary(self):
        return Worker.calculate_salary() + (self.hourly_rate * self.number_of_hours)
    
    worker = Employee(1, 'John Doe', 50000)
    print(worker)
    worker.display()
    