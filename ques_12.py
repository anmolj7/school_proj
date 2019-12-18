'''
Write a program to write those lines which have the character p from one text file to another
text file.
'''

def main():
    fName = input('Enter the name of first file: ')
    with open(fName) as f:
        data = f.readlines()

    data = [line for line in data if line[0].upper() == 'P'] #Filtering lines.
    
    with open(input('Enter the output file\'s name: '), 'w') as f:
        f.writelines(data)

if __name__ == "__main__":
    main()