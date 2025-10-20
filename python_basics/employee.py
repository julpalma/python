from person import Person
#Employee class inherits from Person class

class Employee(Person):
    def __init__(self, name, age, employee_id, role=None):
        #Call the parent constructor
        super().__init__(name, age)
        self.employee_id = employee_id
        self.role = role

    def get_employee_info(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Age: {self.age}, Role: {self.role}"
    
    #Override the greet method
    def greet(self):
        return f"Hello, {self.name}. Welcome to the company!"