permissions = {}
n = int(input("Enter number of files: "))
for _ in range(n):
    m = input("Enter name of file and permissible operation: ").split()
    permissions[m[0]] = set(m[1:])
for _ in range(int(input("Enter number of requests to the files: "))):
        perm, file = input("Enter request: operation and file: ").split()
        if perm == 'read':
            perm = 'R'
        if perm == 'write':
            perm = 'W'
        if perm == 'execute':
            perm = 'X'
        if perm in permissions[file]:
            print('OK')
        else:
            print('Access denied')
