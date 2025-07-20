from Vehicle import Vehicle

class Rental(Vehicle):
    def __init__(self, license_number, vehicle_name, make, model, price, year, number_of_days, rate_per_day):
        super().__init__(license_number, vehicle_name, make, model, price, year)
        self.number_of_days = number_of_days
        self.rate_per_day = rate_per_day
    
    def set_number_of_days(self, number_of_days):
        self.number_of_days = number_of_days
    
    def set_rate_per_day(self, rate_per_day):
        self.rate_per_day = rate_per_day

    def get_number_of_days(self):
        return self.number_of_days
    
    def get_rate_per_day(self):
        return self.rate_per_day

    def calculate_rental_price(self):
        return self.number_of_days * self.rate_per_day
    
    def __str__(self):
        return "License Number: {}, Vehicle Name: {}, Price: ${}, Rental Info: "\
               "Number of Days: {}, Rate per Day: ${:.2f}, Total Rental Price: ${:.2f}".format(
            self.license_number, self.vehicle_name, self.price, 
            self.number_of_days, self.rate_per_day, self.calculate_rental_price()
        )
