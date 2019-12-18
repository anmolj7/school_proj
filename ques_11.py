'''
Write a program to count the number of vowels present in a text file.
'''

def main():
    fName = input('Enter the file name: ')
    with open(fName) as f:
        data = f.read()
    
    count = 0 
    Vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in Vowels:
        count += data.count(vowel)
    print('There are {} vowels in the given file.'.format(count))


if __name__ == "__main__":
    main()