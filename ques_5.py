'''
Write a program to input a character and to print whether a given character is an alphabet, digit
or any other character.
'''

def main():
    char = input('Enter a character: ')
    assert len(char) == 1, "Invalid Length of Character"
    if char.isdigit():
        print('The character is a digit.')
    elif char.isalpha():
        print('The character is an alphabet.')
    else:
        print('The given character is some other character.')

if __name__ == "__main__":
    main()