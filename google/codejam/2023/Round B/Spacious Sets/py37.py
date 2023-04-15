'''
https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad2ce
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
    n,k = reads()
    a = reads()
    asort = list(a)
    asort.sort()
    def helper(arr):
        ans = [1]
        pi = 0
        for ii in range(1, n):
            curr = arr[ii]
            if abs(curr - arr[pi]) >= k:
                while pi+1<ii and abs(curr - arr[pi+1]) >= k:
                    pi += 1
                ans.append(1 + ans[pi])
                pi += 1
            elif pi == 0:
                ans.append(1)
            else:
                ans.append(1 + ans[pi-1])
        return ans
    lll = helper(asort)
    rrr = helper(asort[::-1])
    rrr.reverse()
    ans = dict()
    for ii in range(n):
        aa = asort[ii]
        ll = lll[ii]
        rr = rrr[ii]
        ans[aa] = ll + rr - 1
    return [ans[aa] for aa in a]
for tc0 in range(read()):
    ans = once()
    if not isinstance(ans, (list, tuple)):
        ans = [ans]
    print(f'Case #{tc0+1}:', *ans)
