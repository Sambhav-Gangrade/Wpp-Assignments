class Employee:
    def __init__(self, designation, compensation):
        self.designation = designation  
        self.compensation = compensation  

    def __add__(self, other):
        new_designation = self.designation + " & " + other.designation
        new_compensation = self.compensation + other.compensation
        return Employee(new_designation, new_compensation)

    def __sub__(self, other):
        salary_difference = abs(self.compensation - other.compensation)
        return salary_difference

    def __lt__(self, other):
        return self.compensation < other.compensation

    def __gt__(self, other):
        return self.compensation > other.compensation

    def __eq__(self, other):
        return self.compensation == other.compensation

    def show_details(self):
        print(f"Employee Designation: {self.designation}, Compensation: {self.compensation}")
emp_one = Employee("Senior Developer", 50000)
emp_two = Employee("Project Manager", 60000)
emp_three = Employee("Junior Analyst", 45000)
combined_emp = emp_one + emp_two
combined_emp.show_details()
print("Salary Difference:", emp_one - emp_two)
print("Is emp_one compensation less than emp_two?", emp_one < emp_two)
print("Is emp_two compensation greater than emp_three?", emp_two > emp_three)
print("Is emp_one compensation equal to emp_three?", emp_one == emp_three)