# average at given number
n=int(input('enter the number ')) # how many numbers
s=0 #initialize variable
for i in range(1,n+1):
    s+=i

average_at_number=s/n

print(average_at_number)