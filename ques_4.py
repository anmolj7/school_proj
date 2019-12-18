'''
Write a program to generate random numbers between 1 to 5.
'''
from random import randint 

def main():
    n = int(input("Enter the number of random numbers you want: "))
    for _ in range(n):
        print(randint(1, 5))

if __name__ == "__main__":
    main()