str = input("Enter the string: ")
word = str.split()
wordcount = len(word)
dc,lc,uc,wc,sc = 0,0,0,0,0
for pf in str:
    if pf.isdigit():
        dc+=1
    elif pf.isupper():
        uc+=1
    elif pf.islower():
        lc+=1
    else:
        sc+=1

print(dc, lc,uc ,sc)