from address import Address
from Employee import Employee
from Manager import Manager
from Worker import Worker
from PieceWorker import Pieceworker 

def main():
    print("=== Employee Registration ===")

    
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

    print("\n=== End of Registration ===")

    print("=== Manager Registration ===")
    manager_id = int(input("Enter manager ID: "))
    manager_name = input("Enter manager name: ")
    manager_dept_id = int(input("Enter manager department ID: "))
    manager_country = input("Enter manager country: ")
    manager_city = input("Enter manager city: ")
    manager_zip_code = input("Enter manager zip code: ")
    no_of_subordinates = int(input("Enter number of subordinates: "))
    performance_bonus = float(input("Enter performance bonus: "))
    manager_address = Address(manager_country, manager_city, manager_zip_code)
    manager = Manager(manager_id, manager_name, manager_dept_id, manager_address, no_of_subordinates, performance_bonus)
    print(manager)
    print("=== Manager Details ===")
    manager.display()
    print("Calculated Salary: {:.2f}".format(manager.calculate_salary()))
    print("=== End of Manager Registration ===")

    print("=== Hourly Worker Registration ===")
    worker_id = int(input("Enter worker ID: "))
    worker_name = input("Enter worker name: ")
    worker_dept_id = int(input("Enter worker department ID: "))
    worker_country = input("Enter worker country: ")
    worker_city = input("Enter worker city: ")
    worker_zip_code = input("Enter worker zip code: ")
    no_of_hours_worked = int(input("Enter number of hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    worker_address = Address(worker_country, worker_city, worker_zip_code)
    worker = Worker(worker_id, worker_name, worker_dept_id, worker_address, no_of_hours_worked, hourly_rate)
    print(worker)   
    print("=== Worker Details ===")
    print("Calculated Salary: {:.2f}".format(worker.calculate_salary()))
    print("=== End of Worker Registration ===")


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
    print(Pieceworker(piece_id, piece_name, piece_dept_id, piece_address, no_of_pieces_produced, rate_per_piece))
    


if __name__ == "__main__":
    main()
