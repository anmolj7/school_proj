'''
Write a recursive pyhton program to test if a string is palindrome or not.
'''

def is_palin(String: str, index: int):
    #print(index, String[index], String[-index-1])
    if String[-index-1] != String[index]:
        return False
    if index == 0:
        return True 
    else:
        return  is_palin(String, index-1)

def main():
    String = input("Enter a string: ")
    if is_palin(String, len(String)-1):
        print('The given string is palindrome.')
    else:
        print('The given string is not palindrome.')

if __name__ == "__main__":
    main()
