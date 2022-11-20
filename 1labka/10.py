a = int(input())
b = int(input())
c = int(input())

if a > c:
    z = a
    a = c
    c = z
if a > b:
    z = a
    a = b
    b = z
if b > c:
    z = b
    b = c
    c = z
print(a,b,c)
