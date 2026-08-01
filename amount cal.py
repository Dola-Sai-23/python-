pname=input("enter product name:")
rate=int(input("enter product rate:"))
Qty=int(input("enter product Quality:"))
amount=rate*Qty
print("amount:",amount)
disc=amount*10//100
print("disc:",disc)
net=amount-disc
print("Net Amount:",net)
