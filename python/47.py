
x=1
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    x = 1  
    for k in range(1,i+1):
        print(' ', x, sep='', end='')
        x = x * (i - k) // k
    print()
