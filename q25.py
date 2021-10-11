word='this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated'
c=word.count(" ")+1
avg=(len(word)- word.count(" "))/c
print(avg)