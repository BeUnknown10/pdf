str1 = input("enter string 1: ")
str2 = input("Enter string 2: ")
matchcount=0
short = min(len(str1), len(str2))
long = max(len(str1), len(str2))
for i in range(0, short):
    if str1[i]==str2[i]:
        matchcount+=1
    p = matchcount/long*100
print("percentage: ",p)