hours=input('Enter Hours from Monday     to sunday :')
wage=int(input('Enter Wage per hour:'))
hours=hours.split()
week_hours=[int(x) for x in hours]
total_hours=sum(week_hours)
if total_hours<=40:
    total_wages=total_hours*wage
else:
    overtime=total_hours-40
    total_wages=40*wage+overtime*wage*1.5
print('Total wages:',total_wages )