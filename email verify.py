# email verify
import re
pattern="[a-z0-9]+@[a-z]+\.(com|edu|in|net)"
user_input=input("Enter your email id: ")

if(re.search(pattern, user_input)):
    print("Valid email")
else:
    print("Invalid email")
    user_input=input("Enter your email id: ")


#password verify
import re
pattern=re.compile(r'')
while True:
    password=input("Enter your password here: ")
    if(len(password)<6):
        print("The password must atleast 6 characters")
    elif re.search(r'[!@#$%&*]',password) is None:
            print('Password must contain atleast one special characters')
    elif re.search(r'\d',password) is None:
         print("Password must contain atleast one digit")
    elif re.search('[A-Z]',password) is None:
         print("Password must contain atleast one Capital letter")
    else:
         print('valid Password')
         exit(0)
         
      
        