'''
Write a program to check a number whether it is palindrome or not
'''

def is_palin(num):
    num = str(num)
    if num == num[::-1]: #Using List spicing and indexing to reverse the list.
        return True 
    return False

def main():
    num = int(input('Enter the number you wanna test: '))
    if is_palin(num):
        print('The number is palindrome.')
    else:
        print('The number isn\'t palindome.')

if __name__ == "__main__":
    main()