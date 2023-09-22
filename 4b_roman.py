str=input("Enter the roman number: ")
d={'I':1, 'V':5, 'X':10, 'C':100, 'D':500, 'M':1000}
i,R=0,0
while i<len(str):
    cv=d[str[i]]
    if i+1<len(str[i]):
        nv=d[str[i+1]]
        if cv>nv:
            R=R+cv
            R+=1
        else:
            R=R+nv-cv
            i=i+2
    else:
        R=R+cv
        i+=1
print("Integer number is: ",R)
