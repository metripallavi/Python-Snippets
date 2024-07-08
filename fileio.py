s = "Fenway is a good pet"

#writing to a file
#with open("test.txt", "w") as f:
    #f.write(s)

fp = open("test.txt", "w")
fp.write(s)
fp.close()

#reading to a file
#with open("dog.txt", "r") as f:
     #s = f.read()
     #print(s)

fp = open("dog.txt", "r")
s = fp.read()
print(s)
fp.close()

#Appending to a file
with open("dog.txt", "w") as f:
    f.write(" Ich schrieb das")

fp = open("dog.txt", "w")
fp.write(s)
fp.close()
