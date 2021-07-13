file1 = open("D:/deepthi class/C98/myfile.txt","r+")
readtext = file1.read()
print(readtext)
print(readtext.split())
print(len(readtext))
lower = 0
upper = 0
for i in readtext :
	if i.isupper() :
		upper+=1
	else :
		lower=+1
print("LowerCase Letters : ", lower)
print("UpperCase Letters : ", upper)