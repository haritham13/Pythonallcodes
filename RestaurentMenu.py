i=int(input('Enter list of entries'))
item=input('Enter Item Name')
cost=input('Enter Cost')
dash = 20 - len(item) - len(cost)
for i in range(i):

        print(item+'-'*dash+'$'+cost)
