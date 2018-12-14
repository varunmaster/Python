import codecs
types_of_encoding = ["utf8", "utf-8"]

fileLoc = "C:\\Users\\vm305\\Desktop\\incomingMovies\\enwiki-20180820-pagelinksCopy.txt"
fileLocNew = "C:\\Users\\vm305\\Desktop\\incomingMovies\\enwiki-20180820-pagelinksCopy1.txt"

for encoding_type in types_of_encoding:
    with codecs.open(fileLoc, mode='r', encoding=encoding_type, errors='ignore') as file, \
            codecs.open(fileLocNew, mode='w', encoding='utf-8', errors='ignore') as fileNew:
        for line in file:
            fileNew.write(line.replace("`","'"))