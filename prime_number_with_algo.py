n1=int(input('enter the first input range number '))
n2=int(input('enter the second input range number '))

for k in range(n1,n2+1):
    flag=0
    for i in range(2,k):
        if k%i==0:
            flag=1
    if flag==0:
        print('prime number ',k)