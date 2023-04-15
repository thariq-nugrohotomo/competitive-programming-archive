'''
https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad086
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

def once():
    m,r,n = reads()
    x = reads()
    ans = []
    ii = 0
    while ii + 1 < n:
        if x[ii+1] - r <= 0:
            ii += 1
        else:
            break
    if x[ii] - r > 0:
        return 'IMPOSSIBLE'
    ans.append(ii)
    for ii in range(ii+1, n-1):
        if x[ii+1] - r > x[ans[-1]] + r:
            if x[ii] - r > x[ans[-1]] + r:
                return 'IMPOSSIBLE'
            ans.append(ii)
    if x[ans[-1]] + r < m:
        if x[ans[-1]] + r < x[-1] - r:
            return 'IMPOSSIBLE'
        ans.append(x[-1])
    return len(ans)
    # paper brute-force solve generate manual test-case level 1,2,3,...
for tc0 in range(read()):
    print(f'Case #{tc0+1}: {once()}')
