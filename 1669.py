"""
1 2 1 - 3 - 4
1 2 2 1 - 4 - 6
1 2 3 2 1 - 5 - 9
1 2 3 3 2 1 - 6 - 12
1 2 3 4 3 2 1 - 7  -  16

diff = 4

diff = 5
1 1 1 - 3
1 2 1 - 4

1 2 1 1  - 5
1 2 2 1 - 6

1 2 2 1 1 - 7
1 2 2 2 1 - 8
1 2 3 2 1 - 9


"""
import sys

a, b = map(int, sys.stdin.readline().split())
if a == b:
    print(0)
else:
    n = int((b - a) ** 0.5)
    if n ** 2 == b - a:
        print(2 * n - 1)
    else:
        z = (b - a) - n ** 2
        if z <= n:
            print(2 * n)
        else:
            print(2 * n + 1)

