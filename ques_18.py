'''
Write a program for bubble sort.
'''

def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


def main():
    arr = eval(input('Enter the list: '))
    bubbleSort(arr)

    print('The sorted list: ', *arr)

if __name__ == "__main__":
    main()