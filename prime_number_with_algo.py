'''
Step 1: Start
Step 2: Read n1 and n2 from user.
Step 3: Initialize variables
        k=n1
Step 5: Repeat the steps until k<=n2
    Step 5.1: Initialize variables
                flag=1
                i=2
    Step 5.2 Repeat the step until i<k
            Step 5.2.1 If remainder of k÷i equals 0
                flag←0
                Go to step 5.3
            Step 5.2.2 i←i+1
    Step 5.3: If flag==0
                Display n is not prime
              else
                Display n is prime
    Step 5.4: k=k+1
Step 6: Stop

'''




n1=int(input('enter the first input range number '))
n2=int(input('enter the second input range number '))

for k in range(n1,n2+1):
    if k>1:
        flag=0
        for i in range(2,k):
            if k%i==0:
                flag=1
        if flag==0:
            print('prime number ',k)