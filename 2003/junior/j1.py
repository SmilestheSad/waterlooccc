t = int(input("Enter tine length:"))
s = int(input("Enter tine spacing:"))
h = int(input("Enter handle length:"))

print(t,s,h)

for i in range(t):
    print("*" + " "*s + "*" + " "*s + "*")

print("*"* (3 + s*2)) 

for i in range(h):
    print(' '*(s+1) + "*" )   