from Rental import Rental
class Bus(Rental):
    def __init__(self, vehicle_number, make, model, price, number_of_days, rate_per_day, driver_cost):
        super().__init__(vehicle_number, make, model, price, number_of_days, rate_per_day)
        self.driver_cost = driver_cost
    
    def set_driver_cost(self, driver_cost):
        self.seating_capacity = driver_cost
    
    def get_driver_cost(self):
        return self.driver_cost
    
    

    def __str__(self):
        return "License Number: {}, Vehicle Name: {}, Price: ${}, Rental Info: "\
               "Number of Days: {}, Rate per Day: ${:.2f}, Total Rental Price: ${:.2f}, Driver Cost: ${:.2f}".format(
            self.license_number, self.vehicle_name, self.price, self.number_of_days, 
            self.rate_per_day, self.calculate_rental_price(), self.driver_cost)