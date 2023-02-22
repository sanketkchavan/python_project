from demo4_employee.employee_module import Employee

Employee.company_name= "TCS"
Employee.company_location= "Pune"

emp1 = Employee()
emp1.emp_id = 101
emp1.emp_name = "Sankey"
emp1.emp_salary = 60000
emp1.emp_performance = "A"

print(emp1.calculate_bonus())

