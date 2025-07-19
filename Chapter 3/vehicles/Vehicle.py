class Vehicle:
    def __init__(self, license_number, vehicle_name, make, model, price,year):
        self.license_number = license_number
        self.vehicle_name = vehicle_name
        self.make = make
        self.model = model
        self.price = price
        self.year = year

    def set_licence_number(self, license_number):
        self.license_number = license_number
    def set_vehicle_name(self, vehicle_name):
        self.vehicle_name = vehicle_name
    def set_make(self, make):
        self.make = make
    def set_model(self, model):
        self.model = model
    def set_price(self, price):
        self.price = price
    def set_year(self, year):
        self.year = year
    def get_licence_number(self):
        return self.license_number
    def get_vehicle_name(self):
        return self.vehicle_name
    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_price(self):
        return self.price
    def get_year(self):
        return self.year
    def price(self):
        return self.price
    def __str__(self):
        return "Vehicle Name: {}, Make: {}, Model: {}, Price: {}, Year: {}".format(
            self.vehicle_name, self.make, self.model, self.price, self.year)