from address import Address
from Employee import Employee
from Manager import Manager
from Worker import Worker
from PieceWorker import Pieceworker

def register_manager():
    print("=== Manager Registration ===")
    manager_id = int(input("Enter manager ID: "))
    manager_name = input("Enter manager name: ")
    manager_dept_id = int(input("Enter department ID: "))
    basic_salary = float(input("Enter basic salary: "))
    country = input("Enter country: ")
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")
    no_of_subordinates = int(input("Enter number of subordinates: "))
    performance_bonus = float(input("Enter performance bonus: "))
    manager_address = Address(country, city, zip_code)
    return Manager(manager_id, manager_name, manager_dept_id, basic_salary,
                   manager_address, no_of_subordinates, performance_bonus)

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
    return Worker(worker_id, worker_name, worker_dept_id, worker_address,
                  no_of_hours_worked, hourly_rate)

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
    return Pieceworker(piece_id, piece_name, piece_dept_id, piece_address,
                       no_of_pieces_produced, rate_per_piece)

def display_employee(employee: Employee):
    print("\n--- Employee Details ---")
    print(employee)
    print("Calculated Salary: {:.2f}".format(employee.calculate_salary()))

def get_employee_data(emp):
    return {
        "Name": emp.get_name(),
        "Type": emp.__class__.__name__,
        "Department ID": emp.get_dept_id(),
        "Address": str(emp.get_address()),
        "Salary": "{:.2f}".format(emp.calculate_salary())
    }

def main():
    print("==== Welcome To Employee Management System ====")
    employees = {}

    while True:
        sentinel = input("\nWould you like to register an employee? (yes/no): ").lower()
        if sentinel == "no":
            break

        print("\nSelect employee type:")
        print("1. Manager")
        print("2. Hourly Worker")
        print("3. Piece Worker")
        choice = input("Enter Your Choice (1-3): ")

        employee = None

        if choice == "1":
            employee = register_manager()
        elif choice == "2":
            employee = register_worker()
        elif choice == "3":
            employee = register_pieceworker()
        else:
            print("Invalid choice.")
            continue

        emp_id = employee.get_id()
        if emp_id in employees:
            print("Employee with ID {} already exists. Overwriting.".format(emp_id))
        employees[emp_id] = employee
        display_employee(employee)

    print("\n==== All Registered Employees (Dictionary Format) ====")
    if not employees:
        print("No employees registered.")
    else:
        employee_dict_output = {}
        for emp_id, emp in employees.items():
            employee_dict_output[emp_id] = get_employee_data(emp)

        print(employee_dict_output)

if __name__ == "__main__":
    main()
