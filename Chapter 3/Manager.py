from Employee import Employee
class Manager(Employee):
    def __init__(self, id, name, dept_id, basic_salary, address, no_of_subordinates,performance_bonus):
           super().__init__(self, id, name, dept_id,basic_salary, address)
           self.no_of_subordinates = no_of_subordinates
           self.performance_bonus = performance_bonus

    def set_no_of_subordinates(self, no_of_subordinates):
        self.no_of_subordinates = no_of_subordinates    
    def set_bonus(self, performance_bonus):
        self.performance_bonus = performance_bonus

    def get_no_of_subordinates(self):
        return self.no_of_subordinates  
    def get_performance_bonus(self):
        return self.performance_bonus
    def calculate_salary(self):       
        return super().calculate_salary() + 0.2*(self.performance_bonus) + 0.1*(self.no_of_subordinates)

    
    def __str__(self): 
        return "Manager: {}, ID: {}, Salary: {:.2f}, Department: {}, Subordinates: {}, Bonus: {:.2f}".format(super().__str__(),self.name, self.id,self.basic_salary, self.no_of_subordinates, self.performance_bonus)
