from address import Address
from Employee import Employee
from Manager import Manager
from Worker import Worker
from PieceWorker import Pieceworker 

def register_employee():
    print("=== Employee Registration ===")
    emp_id = int(input("Enter employee ID: "))
    name = input("Enter employee name: ")
    dept_id = int(input("Enter department ID: "))
    basic_salary = float(input("Enter basic salary: "))
    country = input("Enter country: ")
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")
    emp_address = Address(country, city, zip_code)
    emp = Employee(emp_id, name, dept_id, basic_salary, emp_address)
    print("\n=== Employee Details ===")
    emp.display()
    print("Calculated Salary: {:.2f}".format(emp.calculate_salary()))

def register_manager():
    print("=== Manager Registration ===")
    manager_id = int(input("Enter manager ID: "))
    manager_name = input("Enter manager name: ")
    manager_dept_id = int(input("Enter department ID: "))
    country = input("Enter country: ")
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")
    no_of_subordinates = int(input("Enter number of subordinates: "))
    performance_bonus = float(input("Enter performance bonus: "))
    manager_address = Address(country, city, zip_code)
    manager = Manager(manager_id, manager_name, manager_dept_id, manager_address, no_of_subordinates, performance_bonus)
    print("\n=== Manager Details ===")
    print(manager)
    print("Calculated Salary: {:.2f}".format(manager.calculate_salary()))

def register_worker():
    print("=== Hourly Worker Registration ===")
    worker_id = int(input("Enter worker ID: "))
    worker_name = input("Enter worker name: ")
    worker_dept_id = int(input("Enter department ID: "))
    country = input("Enter country: ")
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")
    no_of_hours_worked = int(input("Enter number of hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    worker_address = Address(country, city, zip_code)
    worker = Worker(worker_id, worker_name, worker_dept_id, worker_address, no_of_hours_worked, hourly_rate)
    print("\n=== Worker Details ===")
    print(worker)
    print("Calculated Salary: {:.2f}".format(worker.calculate_salary()))

def register_pieceworker():
    print("=== Piece Worker Registration ===")
    piece_id = int(input("Enter piece worker ID: "))
    piece_name = input("Enter piece worker name: ")
    piece_dept_id = int(input("Enter department ID: "))
    country = input("Enter country: ")
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")
    no_of_pieces_produced = int(input("Enter number of pieces produced: "))
    rate_per_piece = float(input("Enter rate per piece: "))
    piece_address = Address(country, city, zip_code)
    pieceworker = Pieceworker(piece_id, piece_name, piece_dept_id, piece_address, no_of_pieces_produced, rate_per_piece)
    print("\n=== Piece Worker Details ===")
    print(pieceworker)
    print("Calculated Salary: {:.2f}".format(pieceworker.calculate_salary()))

def main():
    print("Welcome to the Employee Management System")
    sentinel = input("Enter yes/no to continue: ")
    while sentinel.lower() == 'yes':
        print("For Manager       enter 1:")
        print("For Hourly Worker enter 2:")
        print("For Piece Worker  enter 3:")
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                register_manager()
            case '2':
                register_worker()
            case '3':
                register_pieceworker()
            case _:
                print("Invalid choice. Exiting.")
    

if __name__ == "__main__":
    main()
