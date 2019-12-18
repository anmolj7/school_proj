ITEMS = []

def is_empty():
    return ITEMS == []

def push(item):
    ITEMS.append(item)

def pop():
    if is_empty():
        print("Stack Underflow.")
    else:
        ITEMS.pop()

def main():
    print("push <value>")
    print("pop")
    print("print")
    print("quit")
    while True:
        command = input("> ")
        if command == 'pop':
            pop()
        elif command == 'quit':
            exit()
        elif command == 'print':
            print(*ITEMS, sep=", ")
        else:
            push(command.split()[1])

if __name__ == "__main__":
    main()