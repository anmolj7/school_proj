'''
Write a program to take a number as input and calculate its cube if its an even number otherwise
multiply it by 2.
'''

def main():
    num = int(input("Enter a number: "))
    if num%2 == 0:
        print(num**3)
    else:
        print(num*2)

if __name__ == "__main__":
    main()