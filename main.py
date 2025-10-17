from employee import Employee

def main():
    # Create a Person object
    person1 = Employee("Juliana", 35, "E123", "Developer")
    
    # Call the greet method
    print(person1.greet())

    #Call static method. Inherited from Person class
    print(person1.message())

    #Call static variable
    print(f"{person1.name} is from {person1.country}")

    print(f"{person1.name} is {person1.getAge()} years old.")

    print(f"{person1.get_employee_info()}")

if __name__ == "__main__":
    main()
