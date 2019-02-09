if __name__ == '__main__':
    f=dict()
    for u in range(int(input())):
        name = input()
        score = float(input())
        f[name]=score
    h=list(f.values())
    h.sort()
    # print(f)
    for i in range(len(h)-1,-1,-1):
        if h[i]==max(h):
            continue
        else:
            k=h[i]
            # print(k)
            break
    for l in f:
        if f[l]==k:
            print(l)