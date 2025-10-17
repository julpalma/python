class Person:
    #Static variable, belongs to the class itself.
    country = "USA"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}"
    
    #Instance method, belongs to the instance of the class.
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
    #define a static method. It does have self parameter.
    #It is called on the class itself, not on an instance of the class.
    @staticmethod
    def message():
        return "This is a static message."