n=int(input("Enter the number"))
num=int(input("Enter the num"))
result=" "
while num>0:
    num=num//n
    r=num%n
    if r<=9:
        result=str(r)+result
    else:
            result=chr(r+55)+result
print(result)

