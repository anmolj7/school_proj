import csv

def read():
    with open(input('Enter csv file name: '), newline='') as myFile:
        reader = csv.reader(myFile)
        for row in reader:
            print(row)

def write():
    data = eval(input("Enter the list you wanna write to csv file: "))
    myFile = open(input('Enter the output filename: '), "w")
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)

def main():
    print("1) One for Reading")
    print("2) Two for Writing")
    choice = int(input("Enter Your choice: "))

    assert choice in range(1, 3), "Wrong Choice."

    if choice == 1:
        read()
    else:
        write()


if __name__ == "__main__":
    main()