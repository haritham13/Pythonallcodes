n=int(input('Enter a number n:'))
rev=0
m=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print('reverse number is ',rev)
if m==rev:
    print('the number is palindrome')
else:
    print('the number is not a plaindrome')
