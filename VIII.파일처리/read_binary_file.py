import Person

f = open("data.bin","rb")
data = f.read()

for item in data :
    print(item)
f.close()


person2 = Person("임정훈",40)
f = open("savefile.per","w",encoding="uft-8")