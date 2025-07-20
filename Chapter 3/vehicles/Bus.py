from Rental import Rental

class Bus(Rental):
    def __init__(self, license_number, vehicle_name, make, model, price, year, number_of_days, rate_per_day, driver_cost):
        super().__init__(license_number, vehicle_name, make, model, price, year, number_of_days, rate_per_day)
        self.driver_cost = driver_cost

    def set_driver_cost(self, driver_cost):
        self.driver_cost = driver_cost  

    def get_driver_cost(self):
        return self.driver_cost

    def __str__(self):
        return "License Number: {}, Vehicle Name: {}, Price: ${}, Rental Info: "\
               "Number of Days: {}, Rate per Day: ${:.2f}, Total Rental Price: ${:.2f}, Driver Cost: ${:.2f}".format(
            self.license_number, self.vehicle_name, self.price, self.number_of_days,
            self.rate_per_day, self.calculate_rental_price(), self.driver_cost)
