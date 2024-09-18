n = int(input())
k = str(n)
intK = int(len(k))
sum = 0 
sum =(n+1-10**(intK-1))*(intK)

for i in range(len(k)-1):
    # 120 이면 3자리 -> i+1,해서 1 2 3 만들고
    sum += 9*(10**i)*(i+1)
print(sum)