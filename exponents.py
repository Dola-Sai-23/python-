a=int(input())
b=int(input())
maxexp=0
maxnum=0
for i in range(a,b+1):
    count=0
    n=i
   
    while(n%2==0):
            count=count+1
            n=n/2
    if count>maxexp:
        maxexp=count
        maxnum=i
        
print("max number:",maxnum)
           

