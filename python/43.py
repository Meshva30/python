x = 65
for i in range(1,6):
    x=65
    for j in range(1,6):
        if(i==1 or i==5 or j==1 or j==5):
            print(chr(x),'',end='')
        else:
            print('  ',end='')
        x+=1
    print()