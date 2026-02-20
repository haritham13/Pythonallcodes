# n=int(input('Enter a Number'))
# count=0
#
# for i in range(1,n+1):
#    if n%i ==0:
#         count+=1
# if count==2:
#     print('given number',n,'is a prime number')
# else:
#     print('given number', n, 'is not a prime number')

#prime numbers from 1 to 100
# n=101

for n in range(1,101):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count ==2:
     print(n)