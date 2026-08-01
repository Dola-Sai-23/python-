#HCF (or) GCD
"""
a=int(input("a:"))
b=int(input("b:"))
if(a<b):
    s=a
else:
    s=b
for i in range(s,0,-1):
    if(a%i==0 and b%i==0):
        print(i)
        break
    """
a=input("enter the number:")
z=len(a)
a=int(a)
l=a%10
a=a//10
m_v=a%(10**(z-2))
a=a//(10**(z-2))
r=l
r=r*(10**(z-2))
r=r+m_v
r=r*10
r=r+a
print(r)



