'''
Write a program for linear search.
'''

def search(arr, element):
    for i in arr:
        if i == element:
            return True 
    return False 

def main():
    arr = eval(input('Enter the list: '))
    element = eval(input('Enter the element to be found: '))
    if search(arr, element):
        print('The given element is present in the list.')
    else:
        print('The given element is not present in the list.')

if __name__ == "__main__":
    main()
    