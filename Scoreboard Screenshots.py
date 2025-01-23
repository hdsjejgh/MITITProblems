amount = int(input().split()[0])
ss = []
for i in range(amount):
    ss.append(list(map(int,input().split())))
unsorted = ss.copy()
ss.sort()
#print(ss)
def hhh():
    columns = []
    for i in range(len(ss[0])):
        columns.append([ii[i] for ii in ss])
    for c in columns:
        cc = c.copy()
        c.sort()
        if c != cc:
            print("NO")
            return
    print("YES")
    result = ""
    for i in ss:
        iiii = unsorted.index(i)
        result+=str(unsorted.index(i)+1)+" "
        unsorted[iiii] = None

    print(result)
hhh()