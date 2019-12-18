'''
Write a program to check if a given number is prime or not.
'''

def is_prime(num):
    for i in range(2, int(num**0.5)):
        if num%i == 0:
            return False 
    return True

def main():
    num = int(input('Enter the number you wanna test: '))
    if is_prime(num):
        print('The number is prime.')
    else:
        print('The number isn\'t prime')

if __name__ == "__main__":
    main()