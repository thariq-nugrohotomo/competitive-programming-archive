'''
https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad9c1
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

MAX = 1111
stoi = {'RPS'[ii]:ii for ii in range(3)}
def once():
    c = read(str)
    a = [stoi[cc] for cc in c]
    x = [1]*3
    x[a[0]] = 0
    aa = a[1]
    y = dict()
    for yi in range(3):
        yy = 0 if yi == aa else 1
        for xi in range(3):
            if yi != xi:
                y[(yi,xi)] = yy + x[xi]
    x = y
    for jj in range(2,len(a)):
        aa = a[jj]
        y = dict()
        for yi in range(3):
            yy = 0 if yi == aa else 1
            for (xi,start),val in x.items():
                if xi!=yi:
                    key = yi,start
                    prev = y.get(key, MAX)
                    if yy + val < prev:
                        y[key] = yy + val
        x = y
    ans = [val for (last,start),val in x.items() if last!=start]
    return min(ans)
    # paper brute-force solve generate manual test-case level 1,2,3,...
for tc0 in range(read()):
    print(f'Case #{tc0+1}:', end=' ')
    print(once())
