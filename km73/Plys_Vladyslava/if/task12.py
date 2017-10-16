n = int(input("n="))
m = int(input("m="))
k = int(input("k="))

if (n%2==0 or m%2==0) & k<n*m & (k%n==0 or k%m==0):
    print("YES")

else:
    print("NO")
