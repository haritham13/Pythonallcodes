pwd1=input('Enter New Password:: ')
pwd2=input("Enter same password:: ")
if pwd1==pwd2:
    print('The Password is changed')
elif pwd1.casefold() == pwd2.casefold():
    print('please check cases and try again')
else:
    print("Password doesnt match")
