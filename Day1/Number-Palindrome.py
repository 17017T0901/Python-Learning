n = int(input())
a = n
rev = 0
while n>0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

if a == rev:
    print("The {} value is palindrome".format(a))
else:
    print("The {} value is not palindrome".format(a))
# other way
n = int(input())
res = int(str(n)[::-1])
if n == res:
    print("{} is palindrome".format(n))
else:
    print("{} is not palindrome".format(n))

#output
#121
#121 is palindrome
