class palindrome:
    def __init__(self):
        self.pali = False
    def ispali(self,str):
        if(str == str[::-1]):
            self.pali = True
        else:
            self.pali = False
        return self.pali

class paliint(palindrome):
    def __init__(self):
        self.pali = False
    def ispali(self, num):
        temp = num
        rev = 0
        while num!=0:
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if (temp==rev):
            self.pali = True
        else:
            self.pali = False
        return self.pali
m = paliint()            
num = int(input("Enter the number: "))
p = m.ispali(num)
if(p==True):
    print(num," is a palindrome")
else:
    print(num," is not a palindrome")
s = palindrome()
str = input("Enter the string: ")
q = s.ispali(str)
if(q==True):
    print(str," is palindrome")
else:
    print(str," is not a palindrome")