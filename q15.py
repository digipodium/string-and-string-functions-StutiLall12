#Ask user to input a sentence and print each word on a different line.
str=input("Write down a sentence")
words=str.split()
for i in words:
    print(f"{i}\n")
