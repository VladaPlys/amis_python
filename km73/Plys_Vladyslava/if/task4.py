a=int(input())
if a%4==0 & a%100!=0 or a%400==0:
    print("LEAP")
else:
    print("COMMON")
