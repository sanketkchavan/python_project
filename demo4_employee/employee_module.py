class Employee:
    company_name= None
    company_location= None

    def __init__(self):
        self.emp_id = None
        self.emp_name = None
        self.emp_salary = None
        self.emp_performance = None

    @staticmethod
    def print_author_name():
        print("Author name: ", "Sanket Chavan")

    def display_employee_record(self):
        print(35 * "-")
        print("Employee ID: ", self.emp_id)
        print("Employee Name: ", self.emp_name)
        print("Employee Salary: ", self.emp_salary)
        print("Employee performance: ", self.emp_performance)
        print("Company name: ", Employee.company_name)
        print("Company location: ", Employee.company_location)
        print(35 * "-")

    def calculate_bonus(self):
        self.display_employee_record()
        if self.emp_performance == 'A':
            print(self.emp_name)
            print("10%")
            self.emp_salary = self.emp_salary + ((10/100) * self.emp_salary)
            print("Updated salary: ", self.emp_salary)
        elif self.emp_performance == 'B':
            print(self.emp_name)
            print("5%")
        elif self.emp_performance == 'C':
            print(self.emp_name)
            print("2%")
        else:
            print(self.emp_name, "will not receive bonus")

