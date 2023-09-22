import os
n,c=0,0
filename = input("Enter the file name: ")
if os.path.exists(filename)==True:
    print(filename, "is present")
else:
    print(filename,"not found")
    exit()
lines = int(input("Enter the number of lines to print: "))
file = open(filename,'r')
listline = file.readlines()
for i in range(lines):
    print(listline[i])

word = input("Enter the word to find its frequency of occurance: ")
for line in listline:
    c+=line.count(word)
print(c)
