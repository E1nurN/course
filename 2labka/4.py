a = int(input())
san = 0;

for i in range (1,a+1):
    san += int(input());
    if(a == i):
        break;
print(san)
