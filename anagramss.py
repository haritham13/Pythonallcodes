phrase1=input('Enter a string1:: ')
phrase2=input('Enter a string 2:: ')
phrase1=phrase1.lower()
phrase2=phrase2.lower()
for x in phrase1:
    if x.isalpha():
        if phrase1.count(x) !=phrase2.count(x):
            print("Not anagrams")
            break
else:
           print("Anagrams")