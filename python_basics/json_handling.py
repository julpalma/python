import json 

def main():
    jsonString = '{"age": 30, "name": "John", "city": "New York"}'

    try:
        # Parse JSON string to dictionary
        data = json.loads(jsonString)
        print(data)
    except json.JSONDecodeError:
        print(f"Error decoding JSON")

    pythonDict = {
        'name': 'Alice',
        'age': 25,
        'city': 'Los Angeles'
    }

    try:
        # Convert dictionary to JSON string
        jsonOutput = json.dumps(pythonDict)
        print(jsonOutput)
    except (TypeError, OverflowError):
        print("Error encoding to JSON")
    except json.JSONDecodeError:
        print(f"Error decoding JSON")


if __name__ == "__main__":
    main()


