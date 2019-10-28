f = open("file.txt","r", encoding="utf8")    # r : read

text = f.read()
print(text)

f.close()

# 인코딩 : 컴퓨터가 알아듣게  디코딩 : 사람이 알아듣게

#한줄씩읽기
f = open("file.txt","r", encoding="utf8")

text0 = f.readline()
print(text0)
text1 = f.readline()
print(text1)

f.close()
# open 과 close는 반드시 있어야 한다