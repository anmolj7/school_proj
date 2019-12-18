'''
Write a program to count number of words in a text file.
'''

def main():
    with open(input('Enter the file\'s name: ')) as f:
        data = f.read()

    data = data.split()
    data = [word for word in data if len(word) > 0] #Filtering empty words.

    print(len(data))

if __name__ == "__main__":
    main()