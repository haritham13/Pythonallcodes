num1=input('Enter values :')
num2=num1.split()
res=[]
for i in num2:
    if i not in res:
        res.append(i)
print(res)
