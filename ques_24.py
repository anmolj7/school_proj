'''
Write a program to find the most common words in a file.
'''

def main():
    with open(input('Enter the name of the file: ')) as f:
        data = f.read()

    data = data.split()
    data = [word for word in data if len(word) > 0]

    freq_dict = {word: data.count(word) for word in data}

    max_value = max(freq_dict.values())

    for key in freq_dict:
        if freq_dict[key] == max_value:
            break 
    
    print('The most common word in the given file is "{}".'.format(key))

if __name__ == "__main__":
    main()