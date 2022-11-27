a = int(input())
san = 0
for i in range (0,10):
    if(a < 1):
        break;

    if(a % 10 == 1):
        san += 2**i
        
    a //= 10
print(san)
