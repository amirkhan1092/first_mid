#LCM
X,Y=eval(input('enter the two number comma separated'))


for k in range(1,(X*Y+1)):
    if k%X==0 and k%Y==0:
        result=k
        break

print('LCM of given Number ',result)


#GCD
X,Y=eval(input('enter the two number comma separated'))
Num=X if X>Y else Y
for k in range(1,Num+1):
    if X%k==0 and Y%k==0:
        Result=k
print('GCD of given number is  ',Result)