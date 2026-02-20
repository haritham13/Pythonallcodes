#Removing unnecessary characters from the input
text=input('Enter some text ::')
scan=''
for x in text:
    if x.isalpha() or x.isspace():
        scan=scan+x
    else:
        scan=scan+' '
print(scan)
