x=int(input('''enter no of rows for all the 10 patterns
            and #NOTE:10 th pattern only works with the 5 rows:-'''))
n=x
y=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
print('\n1st pattern\n')
for i in range(x):
    print('*'*(i+1))
    
print('\n2nd pattern\n')
for i in range(x,0,-1):
    print('*'*i)
print('\n3rd pattern\n')
for i in range(x):
    print('*'*(i+1))
for i in range(x-1,0,-1):
    print('*'*i)

print('\n4th pattern\n')
for i in range(x):
    if i==x//2:
        print(' '*(x-i),end='')
        print('*'*(2*x),end='')
    else:
        print(' '*(n-i),end='')
        print('*'+' '*(2*i)+'*',end='')
    print()

print('5th pattern')
for i in range(x):
    for j in range(5):
        print(y[i]+' ',end='')
    print()
print('\n6th pattern\n')
for i in range(x):
    for j in range(x):
        print(y[j]+' ',end='')
    print()
print('\n7th pattern\n')
for i in range(x):
    print(' '*(n-i),end='')
    for j in range(i):
        print(y[j]+" ",end='')
    print()
    print(' ',end='')

print('\n8th pattern\n')
z=3
for i in range(1,x+1,1):
    print(' '*(x-i),end='')
    if i==1:
        print(y[0]+' ',end='')
        print()
        continue
    for j in range(0,z,1):
        print(y[j]+" ",end='')
    z+=2
    print()
print('\n9th pattern\n')
z=3
for i in range(1,x+1,1):
    print(' '*(x-i),end='')
    if i==1:
        print(y[0]+' ',end='')
        print()
        continue
    for j in range(0,z,1):
        print(y[j]+" ",end='')
    z+=2
    print()
z=x+4
for i in range(x,-1,-1):
    if i==x:
        z=z-2
        continue
    else:
        print(' '*(x-i),end='')
        for j in range(0,z,1):
            print(y[j]+" ",end='')
    z-=2
    print()

print('\n10th pattern\n')
width=x+4
for i in range(x,0,-1):
    print(' '*(x-i),end='')
    for j in range(width):
        print(y[j],end='')
    width-=2
    print()
width=3
for k in range(1,x):
    print(' '*(x-k-1),end='')
    for h in range(width):
        print(y[h],end='')
    width+=2
    print()
        


        
        





















