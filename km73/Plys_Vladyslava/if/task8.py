x1 = int(input("Ввести першу координату першої клітини"))
y1 = int(input("Ввести другу координату першої клітини"))
x2 = int(input("Ввести першу координату другої клітини"))
y2 = int(input("Ввести другу координату другої клітини"))
if x2==x1 & y2==y1+1:
    print("YES")
elif x2==x1+1 & y1==y2:
    print("YES")
elif x1==x2 & y2==y1-1:
    print("YES")
elif y1==y2 & x2==x1-1:
    print("YES")
elif x2==x1+1 & y2==y1-1:
    print("YES")
elif x2==x1-1 & y2==y1-1:
    print("YES")
elif x2==x1+1 & y2==y1+1:
    print("YES")
elif x2==x1-1 & y2==y1+1:
    print("YES")
else:
    print("NO")
    
