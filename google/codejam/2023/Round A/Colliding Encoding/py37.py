'''
https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad7cf
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
    d = reads()
    n = read()
    s = [read(str) for ii in range(n)]
    a = []
    for ss in s:
        aa = [d[ord(sss)-ord('A')] for sss in ss]
        a.append(tuple(aa))
    b = set(a)
    if n == len(b):
        return 'NO'
    else:
        return 'YES'
for tc0 in range(read()):
    print(f'Case #{tc0+1}: {once()}')
