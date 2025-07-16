from address import Address
from Employee import Employee

def main():
   ''' print("=== Employee Registration ===")

    
    emp_id = int(input("Enter employee ID: "))
    name = input("Enter employee name: ")
    dept_id = int(input("Enter department ID: "))
    basic_salary = float(input("Enter basic salary: "))

    
    print("\n--- Address Details ---")
    country = input("Enter country: ")
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")

    
    emp_address = Address(country, city, zip_code)
    emp = Employee(emp_id, name, dept_id, basic_salary, emp_address)


    print("\n=== Employee Details ===")
    emp.display()
    print("Calculated Salary: {:.2f}".format(emp.calculate_salary()))

    print("\n=== End of Registration ===")'''

print("=== Piece Employee Registration ===")
piece_id = int(input("Enter piece worker ID: "))
piece_name = input("Enter piece worker name: ")         
piece_dept_id = int(input("Enter piece worker department ID: "))
piece_country = input("Enter piece worker country: ")
piece_city = input("Enter piece worker city: ")
piece_zip_code = input("Enter piece worker zip code: ")
no_of_pieces_produced = int(input("Enter number of pieces produced: "))
rate_per_piece = float(input("Enter rate per piece: "))
piece_address = Address(piece_country, piece_city, piece_zip_code)
piece_worker = Pieceworker(piece_id, piece_name, piece_dept_id, piece_address, no_of_pieces_produced, rate_per_piece)
print("\n=== Piece Worker Details ===")
print(piece_worker)

if __name__ == "__main__":
    main()
