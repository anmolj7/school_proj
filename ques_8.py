'''
Write a program to print fibonacci series using recursion.
'''

def recur_fibo(n):
    if n <= 1:
       return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

def main():
    n_terms = int(input('Enter the number of terms: '))
    if n_terms < 0:
        raise ValueError("The number can't be less than zero")
    
    for i in range(n_terms):
        print(recur_fibo(i))


if __name__ == "__main__":
    main()