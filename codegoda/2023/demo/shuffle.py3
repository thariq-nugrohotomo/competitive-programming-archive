# https://unstop.com/hackathons/codegoda-2023-agoda-600316
# Coding Round: Demo

def cast(*args):
    return list(map(*args))
def read(dtype=int):
    return dtype(input().strip())
def reads(dtype=int):
    return cast(dtype,input().split())
def decompose(s):
    a = '''
    zero
    one
    two
    three
    four
    five
    six
    seven
    eight
    nine
    '''.split()
    def ford(c):
        return ord(c)-ord('a')
    def fcount(s):
        ans = [0]*26
        for cc in s:
            ans[ford(cc)] += 1
        return ans
    aaa = [int(cc) for cc in '0246875319']
    bbb = 'zwuxgsvtoi'
    ccc = [ford(cc) for cc in bbb]
    cnt = fcount(s)
    ans = [0]*10
    for ii in range(10):
        ccnt = cnt[ccc[ii]]
        ans[aaa[ii]] = ccnt
        for cc in a[aaa[ii]]:
            cnt[ford(cc)] -= ccnt
    return ans
for tcid in range(read()):
    s = read(str)[1:-1]
    freq = decompose(s)
    ans = []
    for ii in range(sum(freq)):
        arr = [jj for jj in range(10) if freq[jj]]
        assert arr
        if len(arr)==1:
            nxt = arr[0]
        else:
            lo = 1 if ii==0 else 0
            nxt = [jj for jj in arr if jj>=lo][0]
        freq[nxt] -= 1
        ans.append(nxt)
    print(int(''.join(cast(str, ans))))
