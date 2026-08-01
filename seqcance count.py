l=list(map(int,input().split()))
max=0
count=0
for i in range(len(l)):
    if l[i]==1:
        count=count+1
        if count>max:
            max=count
    else:
        count=0
            
print(max)
    
