"""
n=int(input())
for i in range(n+1):
    print("*"*i)
"""
n=int(input())
a=list(map(int,input().split()))
print(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print(a[i])
            break
        else:
            continue;
        break
       
        
