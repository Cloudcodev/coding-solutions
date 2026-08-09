if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for _ in range(N):
        # Read the command and split it by spaces
        command = input().split()
        action = command[0]
        
        # Execute the corresponding list operation
        if action == 'insert':
            arr.insert(int(command[1]), int(command[2]))
        elif action == 'print':
            print(arr)
        elif action == 'remove':
            arr.remove(int(command[1]))
        elif action == 'append':
            arr.append(int(command[1]))
        elif action == 'sort':
            arr.sort()
        elif action == 'pop':
            arr.pop()
        elif action == 'reverse':
            arr.reverse()
