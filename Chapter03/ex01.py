target = int(input('Please enter an integer: '))
pwd = 5
while pwd > 0:
    root = 0
    while root**pwd < abs(target):
        root += 1
    if root**pwd == abs(target):
        if target > 0 and pwd % 2 == 1:
            print(root, pwd)
        elif target > 0 and pwd % 2 == 0:
            print(root, pwd)
            print(root*-1, pwd)
        elif target < 0 and pwd % 2 == 1:
            print(root*-1, pwd)
    pwd -= 1
