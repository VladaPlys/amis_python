x1 = int(input("Ввести першу координату першої клітини"))
y1 = int(input("Ввести другу координату першої клітини"))
x2 = int(input("Ввести першу координату другої клітини"))
y2 = int(input("Ввести другу координату другої клітини"))
if x1==y1 & y2==x2:
    print("YES")
elif y2-y1==x2-x1:
    print("YES")
elif x1-x2==y2-y1:
    print("YES")
elif x1 == x2 or y1 == y2:
    print('YES')
else:
    print("NO")
