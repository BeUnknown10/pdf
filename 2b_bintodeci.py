
def bintodec(num):
    dec = 0
    i = 0
    while num != 0:
        reminder = num % 10
        dec += reminder * pow(2, i)
        num = num // 10
        i = i + 1
    return dec

def dectohexa(n):
    hexadecinum = ''
    while n != 0:
        temp = 0
        temp = n % 16
        if temp < 10:
            hexadecinum = str(temp) + hexadecinum
        else:
            hexadecinum = chr(temp + 87) + hexadecinum
        n = n // 16
    return hexadecinum

def octatodecimal(n):
    decvalue = 0
    i = 0
    while n:
        lastdigit = n % 10
        n = n // 10
        decvalue += lastdigit * pow(8, i)
        i += 1
    return decvalue

num = int(input("Enter the binary number: "))
dec_result = bintodec(num)
print("Decimal number is: ", dec_result)

hex_num = int(input("Enter the decimal number for hex conversion: "))
hex_result = dectohexa(hex_num)
print("Hexadecimal number is: ", hex_result)

octanum = int(input("Enter the octal number: "))
octa_result = octatodecimal(octanum)
print("Decimal number is: ", octa_result)
