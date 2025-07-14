n = int(input())
a = n
l = len(str(n))
sum = 0
while n>0:
    r = n % 10
    sum = sum + r ** l
    n = n //10

if sum == a:
    print("The {} is Armstrong Number".format(a))
else:
    print("The {} is not armstrong".format(a))

#Output
# 371
# The 371 is Armstrong Number
