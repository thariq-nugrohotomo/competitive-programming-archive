'''
https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cada38
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
    n = read()
    s = reads()
    uniq = {s[0]}
    ans = [s[0]]
    for jj in range(1, n):
        if s[jj] == s[jj-1]:
            continue
        if s[jj] in uniq:
            return 'IMPOSSIBLE'
        uniq.add(s[jj])
        ans.append(s[jj])
    print(*ans, end='')
    return ''
    # paper brute-force solve generate manual test-case level 1,2,3,...
for tc0 in range(read()):
    print(f'Case #{tc0+1}:', end=' ')
    print(once())
