import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie,', 'Murka', 'Simon']
shelfFile['cats'] = cats
shelfFile['somevalue'] = 'somevalue'
shelfFile.close()
