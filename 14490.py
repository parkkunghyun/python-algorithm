"""
약분이란 -> 30 : 4
최대 공약수로 나누는 것!
18:24 = 
최대공약수는 어떻게 구할까? - 4 : 5
10 : 6
10 6 
2,3,4,5,
둘중 더 작은 숫자의 제곱
10 7
그래서 3
거기까지 구하고 안되면 말기!

"""
import math
import sys
input = sys.stdin.readline

n,m = input().split(":")
n = int(n)
m = int(m)

# 15 10 -> 5
# 10 5 -> 0
# 5 -> 0 = 0
# 0 
data = 1
def gcd(a,b):
    global data
    if b == 0:
        data = a
        return
    else:
        gcd(b, a % b)
    

gcd(n,m)
n = n // data
m = m // data
print(f'{n}:{m}')
    
        

