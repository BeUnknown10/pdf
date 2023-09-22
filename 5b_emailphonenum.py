import re
phnum=re.compile(r'\+\d{12}')
email=re.compile(r'^[a-z0-9]+\@[a-z0-9]+\.[a-z0-9]{2,}$')
f=open('emailcheck.txt','r')
for line in f:
    matches = phnum.findall(line)
    for match in matches:
        print(matches)

    matches = email.findall(line)
    for match in matches:
        print(matches)