'''
Write a python function sin(x,n) to calculate the value of sin(x) using its taylor series expansion
up to n terms.
'''
import math 

def nth_term(n, x):
    temp = (2*n-1)
    return (x**temp)/math.factorial(temp)*(-1)**(n-1)

def sin(x, n):
    ans = 0 
    for i in range(1, n+1):
        ans += nth_term(i, x)
    return ans

def main():
    choice = int(input('1) For angle in Degrees\n2) For angle in radians\nYour choice: '))
    assert choice in range(1, 3), "Invalid Choice."
    x = float(input("Enter the value of x: "))
    n = int(input('Enter the value of n: '))

    if choice == 1:
        x *= math.pi/180
    
    print('The value of the given angle is: {}'.format(sin(x, n)))

if __name__ == "__main__":
    main()