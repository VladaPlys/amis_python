a = [int(i) for i in input().split()]
b = int(input())
a.append(b)
a.sort()
a = a[:: - 1]

print(a.index(b) + a.count(b))
