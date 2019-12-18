'''
Write a program for binary search.
'''

def bin_search(arr, element):
    #assumes array is sorted..
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == element:
            return mid 
        elif arr[mid] > element:
            high = mid-1 
        else:
            low = mid+1 
    
    return False 

def main():
    List = list(map(int, input("Enter the numbers seprated by spaces: ").split()))
    List.sort()

    num = int(input('Enter the number you wanna find: '))
    if bin_search(List, num):
        print('The number is present in the given numbers.')
    else:
        print("The number isn't present in the given numbers.")

if __name__ == "__main__":
    main()