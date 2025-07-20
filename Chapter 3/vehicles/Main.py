from Vehicle import Vehicle
from Rental import Rental
from Sale import Sale
from Bus import Bus

def main():
    print("===== Welcome to the Vehicle Management System=========")
    license_number = input("License Number: ")
    vehicle_name = input("Vehicle Name: ")
    make = input("Make: ")
    model = input("Model: ")
    price = float(input("Price: "))
    year = int(input("Year: "))

    vehicle = Vehicle(license_number, vehicle_name, make, model, price, year)

    print("\nVehicle Details:")
    print(vehicle)
    
    print("\n===== Rental Vehicle =====")
    number_of_days = int(input("Enter number of days for rental: "))  
    rate_per_day = float(input("Enter rate per day: "))
    rental_vehicle = Rental(license_number, vehicle_name, make, model, price, year, number_of_days, rate_per_day)   
    print("\nRental Vehicle Details:")
    print(rental_vehicle)
    print("Total Rental Price: ${:.2f}".format(rental_vehicle.calculate_rental_price()))


    print("\n===== Sale Vehicle =====")
    depreciation_rate = float(input("\nEnter depreciation rate (%): "))
    selling_price = float(input("Enter selling price: "))
    sale_vehicle = Sale(license_number, vehicle_name, make, model, price, year, depreciation_rate, selling_price)
    print("\nSale Vehicle Details:")
    print(sale_vehicle)
    print("Depreciation Amount: ${:.2f}".format(sale_vehicle.calculate_depreciation()))
    print("Selling Price: ${:.2f}".format(sale_vehicle.get_selling_price()))
    
    print("\n===== Bus Vehicle =====")
    driver_cost = float(input("Enter driver cost: "))
    bus_vehicle = Bus(license_number, vehicle_name, make, model, price, year, number_of_days, rate_per_day, driver_cost)
    print("\nBus Vehicle Details:")
    print(bus_vehicle)
    print("Total Rental Price with Driver Cost: ${:.2f}".format(
        bus_vehicle.calculate_rental_price() + bus_vehicle.get_driver_cost()))
 
if __name__ == "__main__":
    main()

