import shelve

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
print(shelfFile['somevalue'])
shelfFile.close()
