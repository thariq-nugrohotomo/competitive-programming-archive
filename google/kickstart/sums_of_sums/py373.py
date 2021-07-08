"""
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434819/00000000004348e6
"""
def start():
    from bisect import bisect
    def psum(a):
        ans = [0]*len(a)
        for jj in range(1, len(a)):
            ans[jj] = a[jj] + ans[jj-1]
        return ans
    class bguess:
        __slots__='f'
        def __init__(self, f):
            self.f=f
        def __getitem__(self,x):
            return self.f(x)
    for tc0 in range(int(input())):
        n,q = map(int, input().split())
        a = list(map(int, input().split()))
        blo = min(a)
        bhixx = sum(a)
        a.append(0)
        a.reverse()
        b = psum(a)
        blen = len(b)
        c = psum(b)
        class bsearch:
            __slots__='lft'
            def __getitem__(self, ii):
                return b[ii]-b[self.lft-1]
        bs = bsearch()
        def cntlteq(x):
            col=0
            cnt=0
            magic=19
            for lft in range(1,blen):
                if col+magic>=blen or b[col+magic]-b[lft-1]>x:
                    while col+1<blen and b[col+1]-b[lft-1]<=x:
                        col+=1
                else:
                    bs.lft = lft
                    col=bisect(bs,x,col,blen)-1
                cnt+=col-lft+1
            return cnt
        def sumlteq(x):
            col=0
            sum=0
            magic=19
            for lft in range(1,blen):
                if col+magic>=blen or b[col+magic]-b[lft-1]>x:
                    while col+1<blen and b[col+1]-b[lft-1]<=x:
                        col+=1
                else:
                    bs.lft = lft
                    col=bisect(bs,x,col,blen)-1
                sum+=c[col]-c[lft-1]-b[lft-1]*len(range(lft,col+1))
            return sum
        print('Case #{}:'.format(tc0+1))
        qq=[]
        qset = set()
        for z1 in range(q):
            l1,r1 = map(int, input().split())
            qq.append((r1,l1-1))
            qset.add(r1)
            qset.add(l1-1)
        qset=list(qset)
        qset.sort()
        gmemo = dict()
        bguesscntlteq = bguess(cntlteq)
        def guess(key, blo, bhixx):
            key-=1
            ans = gmemo.get(key)
            if ans != None:
                return ans
            gmemo[key] = ans = bisect(bguesscntlteq, key, blo, bhixx)
            return ans
        smemo = dict()
        def answer(qsval, bval):
            if qsval in smemo:
                return
            pcnt = cntlteq(bval)
            ans = sumlteq(bval)
            ans -= bval*(pcnt-qsval)
            smemo[qsval] = ans
        bhixx = guess(qset[-1],blo,bhixx)
        answer(qset[-1], bhixx)
        blo = guess(qset[0],blo,bhixx)
        answer(qset[0], blo)
        def trec(ql0, qr1, blo, bhixx):
            if qr1-ql0<2:
                return
            qmid = (ql0 + qr1) // 2
            midval = guess(qset[qmid], blo, bhixx)
            answer(qset[qmid], midval)
            trec(ql0,qmid,blo,midval)
            trec(qmid,qr1,midval,bhixx)
        trec(0,len(qset)-1,blo,bhixx)
        for qqq in qq:
            ans = smemo[qqq[0]] - smemo[qqq[1]]
            print(ans)
if __name__ == "__main__":
    start()
