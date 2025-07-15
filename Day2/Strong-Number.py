n = int(input())
a = n
sum = 0
while n > 0:
    r = n % 10
    mul = 1
    for i in range(1,r+1):
        mul = mul * i
    sum = sum + mul
    n = n//10

if a == sum:
    print("The {} is Strong Number".format(a))
else:
    print("The {} is not Strong Number".format(a))

#output
#145
#The 145 is Strong Number
