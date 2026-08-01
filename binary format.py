"""
n=int(input())
a=""
b=""
while n>0:
   r=n%2
   n=n//2
   print(r)
   a=a+str(r)
   b=str(r)+b
   print(b)
"""
num=int(input())
n=0
while num>0:
   if((num and 2**n) == 2**n):
      print("0")
   else:
      print("1")
   
   
