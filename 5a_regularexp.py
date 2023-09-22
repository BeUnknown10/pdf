import re
def isphonenumber(str):
    i=0
    
    if len(str)!=12:
        return False
    elif i==3 or i==7:
        return False
    elif str[i].isdigit()==False: 
        return False
    else:
        return True
str=input("Enter the phone number: ")
isphonenumber(str)
print("Without using the REgular Expressions: ")
if isphonenumber(str)==True:
    print("It is a phone number")
else:
    print("It is not a phone number")

print("With using Regular expressions: ")
def checkphonenumber(str):
    pattern=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pattern.match(str):
        return True
    else:
        return False
checkphonenumber(str)
if isphonenumber(str)==True:
    print("It is a phone number")
else:
    print("It is not a phone number")