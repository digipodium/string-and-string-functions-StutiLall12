#Remove all the special characters and numbers from the following string
text = '%p34@y!*-*!t68h#&on404'
m=''
for i in text:
    if i.isalnum():
        m=m+i
print(m)

    