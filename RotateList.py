num1=input('Enter values :')
num2=num1.split()
rotation=num2[::-1]
n=int(input('number of rotations'))
an1=num2[n:]+num2[:n]
print(rotation)
print(an1)

