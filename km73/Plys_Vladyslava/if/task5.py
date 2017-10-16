a = int (input ("Ввеcти перше число:"))
b = int (input ("Ввести друге число:"))
c = int (input ("Ввести третє число:"))
if (a==b & b!=c) or (a==c & c!=b) or (b==c & c!=a):
    print(2)
elif a==c & b==c:
    print(3)
else:
    print(0)
