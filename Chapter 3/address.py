class Address:
    def __init__(self, country, city, zip_code):
        self.country = country
        self.city = city
        self.zip_code = zip_code

    def __str__(self):
       return "{}, {} - {}".format(self.city, self.country, self.zip_code)


    def display(self):
        return "Address: " + str(self) 
