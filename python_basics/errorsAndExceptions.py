def handleException(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            print(f"ValueError occurred: {ve}")
        except Exception as e:
            print(f"An exception occurred: {e}")
    return wrapper


class HttpException(Exception):
    def __init__(self, status_code, message="HTTP Error occurred"):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{message}: Status Code {status_code}")

    @staticmethod
    @handleException
    def divide_numbers(num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2


def main():
    excep = HttpException(404, "Not Found")
    print(excep)

    print(HttpException.divide_numbers(10, 2))
    print(HttpException.divide_numbers(10, 0))
    print(HttpException.divide_numbers(10, 'a'))


if __name__ == "__main__":
    main()
