x = int(input())
y = int(input())
z = int(input())

def Election(x,y,z):
    if(x == 1 and y == 1 or x == 1 and z == 1 or y == 1 and z == 1):
        return 1
    return 0
print(Election(x,y,z))
