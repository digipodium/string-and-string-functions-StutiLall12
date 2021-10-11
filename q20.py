#Ask user to input string, print found if any of the character is upper case.
str="The Tghyu"
c=0
for i in  str:
    if i.isupper():
        print("Found")
        c=1
        break
if c==0:
    print("not found")
    



