"""

11011

7
7//-2 = -3 - 1
-3 // -2 = 1 - 1

"""

n=int(input())
res=''

print(7 // -2)

if n==0:
    print(0)
    exit
while n!=0:
    print(n)
    if n%(-2)!=0:
        res +='1'
        n=n//(-2)+1
    else:
        res +='0'
        n=n//(-2)

print(res[::-1])


