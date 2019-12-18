'''
Write a program to calculate the factorial of an integer using recursion.
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n*factorial(n-1)

def main():
    num = int(input("Enter the number: "))
    print('The factorial of {} is {}'.format(num, factorial(num)))


if __name__ == "__main__":
    main()