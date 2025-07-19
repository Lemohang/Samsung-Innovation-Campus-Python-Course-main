from Vehicle import Vehicle
class Sale(Vehicle):
    def __init__(self, license_number, vehicle_name, make, model, price, year, depreciation_rate, selling_price):
        super().__init__(license_number, vehicle_name, make, model, price, year)
        self.depreciation_rate = depreciation_rate
        self.selling_price = selling_price
    
    def set_depreciation_rate(self, depreciation_rate):
        self.depreciation_rate = depreciation_rate
    def set_selling_price(self, selling_price):
        self.selling_price = selling_price
    
    def get_depreciation_rate(self):
        return self.depreciation_rate
    
    def get_selling_price(self):
        return self.selling_price

    def calculate_depreciation(self):
        return self.price * (self.depreciation_rate / 100)
    
    def __str__(self):
        return "License Number: {}, Vehicle Name: {}, Price: {}, Depreciation: {:.2f}, Selling Price: {:.2f}".format(
            self.license_number, self.vehicle_name, self.price, 
            self.calculate_depreciation(), self.selling_price
        )