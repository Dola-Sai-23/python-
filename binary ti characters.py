"""
n=int(input())
z=""
while n>0:
    r=n%26
    n=n//26
    z=chr(r+64)+z
print(z)
"""
#alphabets to number
s=input()
n=0
count=0
for i in range(len(s)-1,-1,-1):
    for j in range(len(s)):
        n=s[i]*26**j
        count=count+1
print(len(n))    
    
