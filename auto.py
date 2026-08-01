"""
n=input("enter ")
flag=True
for i in range(len(n)):
    if n.count(str(i))!=int(n[i]):
        flag=False
     # print(" not autobiographic",i,n[i])
if flag==True:
    print("AB")
else:
    print("NAB")
"""
#2nd method:-
#---------------------
d={ }
flag=True
for i in range(len(n)):
    d[i]=0
for i in range (len(n)):
    d[int(n[i])]=d.get(int(n[i]))+1
for i in range(len(n)):
          if d[i]  !=int(n[i]):
              flag=Flase
print(d)
if flag==True:
          print("AB")
else:
    print("NAB")
          
       

