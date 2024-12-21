import sys
input = sys.stdin.readline
#def getInts(): return map(int, input().split())


h, v = '-', '|'
s, n = input().split()
s = int(s)

def construct_segment(n):
    lcd = [[' '] * (s+2) for _ in range(2*s+3)]
    for i in range(1, s+1):
        if n in '02356789':
            lcd[0][i] = h
            
display = [construct_segment(i) for i in n]

for line in zip(*display):
    for r in line:
        print(''.join(r),end=' ')
    print()