'''
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f49d7/0000000000bcf0fd
'''
def read(dtype=int):
    return dtype(input().strip())
def reads(dtype=int):
    return list(map(dtype, input().split()))

i2m = 'NESW'
deltas = [-1, 1, 1, -1]
cycle = list(range(4)) * 3
for tcase0 in range(read()):
    _,r,c,sr,sc = reads()
    memos = [
        [dict() for _ in range(c+11)],
        [dict() for _ in range(r+11)],
        [dict() for _ in range(c+11)],
        [dict() for _ in range(r+11)],
    ]
    sr += 4
    sc += 4
    # print((r, c), (sr, sc))
    for action in read(str):
        # print(action)
        if action in 'NS':
            aa,bb = sr,sc
        else:
            aa,bb = sc,sr
        ptr0 = i2m.index(action)
        dt = deltas[ptr0]
        a2 = memos[ptr0][bb].get(aa+dt, aa+dt)
        # print(f'{aa} --> {a2}')
        for dptr in range(4):
            ptr = ptr0 + dptr
            id = cycle[ptr]
            dt = deltas[id]
            xx,yy = (bb,aa) if dptr % 2 else (aa,bb)
            hi = memos[id][yy].get(xx+dt, xx+dt)
            lo = memos[cycle[ptr+2]][yy].get(xx-dt)
            lo = xx if lo is None else lo+dt
            memos[id][yy][lo] = hi
            # print(i2m[id], (yy,), lo, '-->', hi)
        aa = a2
        if action in 'NS':
            sr,sc = a2,bb
        else:
            sc,sr = a2,bb
        # print(f'{sr} {sc}')
    sr -= 4
    sc -= 4
    print(f'Case #{tcase0 + 1}: {sr} {sc}')
