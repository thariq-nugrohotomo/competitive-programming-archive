'''
https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad9c2
'''
def read(dtype=int):
    return dtype(input().strip())
def reads(dtype=int, coll=list):
    return coll(map(dtype, input().split()))
def fastin():
    import sys
    from io import StringIO
    sys.stdin = StringIO(sys.stdin.read())
from collections import deque

MAX = 1111111111111
dp = [26]
while 1:
    ii = len(dp) + 1
    dp.append(dp[-1] + 26 * ii)
    if dp[-1] > MAX:
        break
dp.insert(0, 0)
def once():
    n = read()
    for jj in range(1,len(dp)):
        if dp[jj-1] < n <= dp[jj]:
            break
    repeat = jj
    start0 = dp[repeat-1]
    n -= start0
    n -= 1
    n = n // repeat
    ans = ord('A') + n
    return chr(ans)
    # paper brute-force solve generate manual test-case level 1,2,3,...
for tc0 in range(read()):
    print(f'Case #{tc0+1}:', end=' ')
    print(once())
