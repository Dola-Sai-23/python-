'''''
s, size = input("Enter string and size: ").split()
size=int(size)
z=' '
for i in range(len(s)):
        if s[i] not in z:
            z=z+s[i]
        if (i+1)% size ==0:
            print(z)
            z=' '
if z:
    print(z)
'''''
s =list(map(int,input().split()))
a=[ ]
for i in range(len(s)):
    z=0
    for j in range(len(s)):
        if i!=j:
            z+=s[j]
    a.append(z)

print(a)
    

        
    

            
                

        
        
