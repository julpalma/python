def main():
    print("Hello, World!")
    name = 'Alice'
    lName = "Smith"
    print(f"Welcome, {name} {lName}!")
    age = 30
    print(f"{name} is {age} years old.")
    type(age)
    print(f"The type of age is {type(age)}.")


#List can be changed. Mutable
    my_list = [1, 2, 3]
    my_list.append(4)
    print(f"My list is: {my_list}")
    print(f"The length of my list is: {len(my_list)}")

#Set cannot have duplicate values. Unordered
    my_set = {1, 2, 3}
    print(f"My set is: {my_set}")

    print(f"The length of my set is: {len(my_set)}")

#Tupple cannot be changed. Immutable
    my_tuple = (1, 2, 3)
    print(f"My tuple is: {my_tuple}")
    print(f"The length of my tuple is: {len(my_tuple)}")
    
#Dictionary key-value pairs. Mutable. Unique keys

    my_dict = {
        'name': 'Alice', 'age': 30}
    print(f"My dictionary is: {my_dict}")
    print(f"The length of my dictionary is: {len(my_dict)}")

def greet(name):
    return f"Hello, {name}!"

def factorial(n):
    if type(n) != int or n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def factorial_mew(n):
    if type(n) != int or n < 0:
        return None
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def listComprehension_example():
    squares = [x**2 for x in range(10)]
    print(f"Squares from 0 to 9: {squares}")

def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def allPrimesUpTo(num):
    if num < 2:
        return set()
    
    prime_numbers = [2]  # start with 2
    for i in range(3, num+1, 2):  # check all odd numbers up to num
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers

#Improvements:
#Handle 2 separately – the only even prime.
#Skip even numbers – after checking 2, no even number can be prime.
#Step 2 in range() – only loops over odd numbers (3, 5, 7…), reducing checks by half.
def isPrimeBetterVersion(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # even numbers > 2 are not prime

    # Only check odd numbers up to sqrt(num)
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def performOperation(a, b, operation='add', message='Default message'):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    
def function(varA, varB):
    print(locals())  # prints local variables

if __name__ == "__main__":
    main()
    greeting = greet("Bob")
    print(greeting)
    fact = factorial(5)
    print(f"Factorial of 5 is: {fact}")
    fact_mew = factorial_mew(5)
    print(f"Factorial (iterative) of 5 is: {fact_mew}")
    fib = fibonacci(6)
    print(f"6th Fibonacci number is: {fib}")
    listComprehension_example()
    fizzBuzz(15)

    #ternary operator: returns one value if condition is true, else another value
    age = 20
    status = "Adult" if age >= 18 else "Minor"
    print(f"Status: {status}")

    fizzBuzz = 'Fizz' if age % 3 == 0 else 'Buzz' if age % 5 == 0 else str(age) 
    print(f"FizzBuzz result for age {age}: {fizzBuzz}")

    allPrimesUpTo(100)
    print(f"All primes up to 100: {allPrimesUpTo(100)}")
    prime_check = isPrimeBetterVersion(29)
    print(f"Is 29 prime? {prime_check}")

    performOperation(10, 5)
    #We can change the default values. operation and message are keyword arguments
    result = performOperation(10, 5, operation='multiply', message='Multiplying numbers')
    print(f"Result of operation: {result}")
    #we can change the order of the keyword arguments
    result2 = performOperation(10, 5, message='Subtracting numbers', operation='subtract')
    print(f"Result of operation 2: {result2}")

    function(1, 2)

    #Lambda function: anonymous function defined with lambda keyword
    result = (lambda x: x**2)(5)  # returns 25
    print(f"Result of lambda function: {result}")


    add = lambda a, b: a + b
    sum_result = add(3, 4)  # returns 7
    print(f"Result of add lambda function: {sum_result}")

    my_list = [1, 4, 5, 2, 3]
    sorted_list = sorted(my_list)        
    print(f"Sorted list: {sorted_list}")


    sorted_descending = sorted(my_list, reverse=True)
    print(f"Sorted list in descending order: {sorted_descending}")

    