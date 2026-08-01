#ANAGRAM:-
#------------------->
"""
d1=input("")
d2=input("")
print(sorted(d1))
print(sorted(d2))
if(sorted(d1)==sorted(d2)):
    print(" an anagram")
else:
    print("not an anagram")
    """
s1='abcdbcd'
s2='dbcdcba'
n={}
for i in s1:
    n[i]=n.get(i,0)+1
print(n)
m={}
for i in s2:
    m[i]=m.get(i,0)+1
print(m)
"""if(n==m):
    print("True")
else:
    print("False")"""
for i in n.keys():
    if n[i] != m[i]:
        print("NA")
        break
else:
    print("A")
