class Worker(Employee):
    def __init__(self, id, name, dept_id, address, no_of_hours_worked, hourly_rate):
        super().__init__(id, name, dept_id, address)
        self.no_of_hours_worked = no_of_hours_worked
        self.hourly_rate = hourly_rate

    def set_no_of_hours_worked(self, no_of_hours_worked):
        self.no_of_hours_worked = no_of_hours_worked

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def get_no_of_hours_worked(self):
        return self.no_of_hours_worked

    def get_hourly_rate(self):
        return self.hourly_rate

    def calculate_salary(self):
        return self.no_of_hours_worked * self.hourly_rate

    def __str__(self):
        return f"Worker: {self.name}, ID: {self.id}, Salary: {self.calculate_salary()}, Department: {self.department}"  