##finding the max and min values
n=int(input('Enter how many number you want : '))
Max=float('-inf')
Min=float('inf')
i=0
print('Enter the numbers: ')
while i < n:
    i=i+1
    x=int(input('enter number: '))
    if x>Max:
        Max=x
    if x<Min:
        Min=x
print('The Maximum of number is:  ',Max)
print('The Minimum of a number is:  ',Min)