import numpy as np

def emi(p, r, t):
    r = r/(12*100)
    t = t*12 
    emi = (p*r*np.power(1+r, t))/(np.power(1+r, t)-1)
    return emi 

def main():
    principal = int(input("Enter the principal amount: "))
    rate = int(input("Enter the rate: "))
    time = int(input('Enter the time: '))

    print('The Monthly EMI is Rs', emi(principal, rate, time))

if __name__ == "__main__":
    main()