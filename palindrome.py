str = input("Enter the  string: ")

def isPalindrome(s):
    return s == s[::-1]

pali = isPalindrome(str)
if(pali==True):
    print("palindrome")
else:
    print("Not palindrome")


num = int(input("Enter the number: "))
temp = num
rev = 0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10

if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")