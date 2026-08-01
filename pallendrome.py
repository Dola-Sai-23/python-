string = input("Enter a string: ")
reversed_string = ""
for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]

print("Reversed string:", reversed_string)
if string==reversed_string:
    print("pallendrome")
else:
    print("not a pallendrome")

