size = int(input("Enter the max_size of the queue: "))           
queue = [None for i in range(size)]  
front = rear = -1

def enqueue(data):
    global rear, size, queue, front
    if (rear+1)%size == front:
        print('Queue is full.')
    elif front == -1:
        front = 0
        rear = 0
        queue[rear] = data
    else:
        rear = (rear+1)%size 
        queue[rear] = data 

def dequeue():
    global rear, size, queue, front
    if front == -1:
        print('Queue is empty.')
    
    elif front == rear:
        temp = queue[front]
        front = -1 
        rear = -1 
        return temp 
    
    else:
        temp = queue[front]
        front = (front+1)%size 
        return temp 

def display():
    global rear, size, queue, front
    if front == -1:
        print('Queue is empty.')
    elif rear >= front:
        print('Elements in the circular queue are: ', end="")
        print(*queue[front:rear+1])
    else:
        print('Elements in the circular queue are: ', end="")
        print(*queue[front:size+1], end=" ")
        print(*queue[:rear+1])

def main():

    print("push <value>")
    print("pop")
    print("print")
    print("quit")
    while True:
        command = input("> ")
        if command == 'pop':
            print("Popped", dequeue())
        elif command == 'quit':
            exit()
        elif command == 'print':
            display()
        elif command.split()[0] == "push":
            enqueue(command.split()[1])
        else:
            print('Wrong Command.')

if __name__ == "__main__":
    main()