n=int(input('Enter how many number you want : '))
Max=0
i=0
print('Enter the numbers: ')
while i < n:
    i=i+1
    x=int(input('enter number: '))
    if x>Max:
        Max=x
print('The Maximum of number is:  ',Max)
