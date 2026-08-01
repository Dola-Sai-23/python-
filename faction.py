"""
n= int(input("enter the numerator "))
n1=int(input("enter the deminator "))
if(n>n1):
    n2=n1
    for i in range(n2,0,-1):
        if(n%i==0 and n1%i==0):
            numerator=n//i
            denominator=n1//i
            print(numerator)
            print(denominator)
            break
else:
    n2=n
    for i in range(n2,0,-1):
        if(n%i==0 and n1%i==0):
            numerator=n//i
            denominator=n1//i
            print(numerator)
            print(denominator)
            break
        """
a=[1,2,3,4,5]
sum=0
for i in range(len(a)):
    sum=sum+a[i]
print(sum)
        

