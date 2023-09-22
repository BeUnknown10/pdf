

def function(num):
    if num==1:
        return 1
    elif num == 0:
        return 0
    else:
        return function(num-1)+function(num-2)
    
num = int(input("Enter the number: "))
a=function(num)
if num>0:
    print("number is ",a)
else:
    print("Error")

