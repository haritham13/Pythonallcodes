item1=input('Enter Item1 :')
price1=input('Enter Item1price :')
item2=input('Enter Item2 :')
price2=input('Enter Item2price :')
item3=input('Enter Item3 :')
price3=input('Enter Item3price :')
item4=input('Enter Item4 :')
price4=input('Enter Item4 price: ')
total_length=20
def print_menu_item(item, price):
    dash_count=total_length-len(item)-len(price)
    dashes='-'*dash_count
    print(item+dashes+price)
print_menu_item(item1, price1)
print_menu_item(item2, price2)
print_menu_item(item3, price3)
print_menu_item(item4, price4)
