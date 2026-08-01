"""
n=list(map(str,input(" ").split()))
print(n)
n="-".join(n)
print(n)
"""
def print_full_name(first, last):
    fullname=first_name+" "+last_name+"!"
    print(fullname)
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
