import csv

def main():

    ## Examples of file reading
    f = open ("example.txt", "r")
    content = f.read()
    print(content)

     #reads only 1 line
    line = f.readline()
    print(line)

    lines = f.readlines()  #reads all lines into a list 
    print(lines)

    #This is same result as f.read
    for line in lines:
        print(line.strip())  #strip() removes extra new lines and spaces    
    
    f.close()  # Re-add the f.close() to properly close the file

    ## Example of file writing
    file = open("output.txt", "w")
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.close()
    print("File written successfully.")

    # ----------------------------------- #

    ## Example of CSV file reading
    with open('data.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        next(csvFile)  # Skip the header (first) row
        for lines in csvFile:
            print(lines)


    with open('data.csv', mode ='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            print(lines)

    with open('data.csv', mode ='r') as file:
        csvFile = list(csv.DictReader(file)) #store all rows in a list
        #Filter names starting with 'A'
        csvFile = [line for line in csvFile if line['Name'].startswith('A')]
        print(csvFile)
    

    with open('output.csv', mode ='w', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow(['Name', 'Age', 'City'])
        csvWriter.writerow(['Alice', 30, 'New York'])
        csvWriter.writerow(['Bob', 25, 'Los Angeles'])
        csvWriter.writerow(['Anna', 25, 'Los Angeles'])
        csvWriter.writerow(['Emma', 25, 'Los Angeles'])
        csvWriter.writerow(['Lily', 25, 'Los Angeles'])
        csvWriter.writerow(['Bree', 25, 'Los Angeles'])


    print("CSV file written successfully.")

if __name__ == "__main__":
    main()