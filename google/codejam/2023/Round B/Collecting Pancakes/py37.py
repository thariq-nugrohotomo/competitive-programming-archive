'''
https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad7d1
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
    a = reads()
    la, ra, lb, rb = reads()
    la -= 1
    lb -= 1
    psum = list(a)
    for jj in range(1,n):
        psum[jj] += psum[jj-1]
    total = psum[-1]
    aaa = []
    for aa in range(la, ra):
        bbb = []
        bl = max(min(aa-1, rb-1), lb)
        if bl < aa:
            assert lb <= bl < rb
            steps = aa - bl - 1
            aaaa = aa - steps // 2
            bbbb = bl + steps // 2
            if steps % 2 != 0:
                aaaa -= 1
            assert bbbb + 1 == aaaa
            bbbb = psum[bbbb]
            aaaa = total - bbbb
            bbb.append((bbbb,aaaa))
        br = min(max(aa+1, lb), rb-1)
        if br > aa:
            assert lb <= br < rb
            steps = br - aa - 1
            aaaa = aa + steps // 2
            bbbb = br - steps // 2
            if steps % 2 != 0:
                aaaa += 1
            assert aaaa + 1 == bbbb
            aaaa = psum[aaaa]
            bbbb = total - aaaa
            bbb.append((bbbb,aaaa))
        assert bl<aa or br>aa
        aaa.append(max(bbb)[1])
    return max(aaa)
    # paper brute-force solve generate manual test-case level 1,2,3,...
for tc0 in range(read()):
    ans = once()
    if not isinstance(ans, (list, tuple)):
        ans = [ans]
    print(f'Case #{tc0+1}:', *ans)
