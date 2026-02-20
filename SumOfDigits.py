n=int(input('Enter a number n:'))
Sum=0
while n>0:
    r=n%10
    Sum=Sum+r
    n=n//10
print(Sum)
