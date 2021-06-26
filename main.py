def F(n:int):
    list = []
    for i in range(2**n):
        b = bin(i)[2:]
        while len(b)<n:
            b = '0' + b
        b = b.replace('1','+')
        b = b.replace('0', '-')
        list.append(b)
    return list

def sinh(k,n,a):
    i = k
    while i > 0 and a[i] == n + i - k:
        i = i - 1
    a[i] = a[i] + 1
    if i > 0:
        for j in range(i+1,n+1):
            a[j] = a[i] + j - i
        return True
    else:
        return False

def tohop(check:True,k,n):
    a = [0]
    comps = []
    for i in range(1, n+1):
        a.append(i)
    while check:
        comps.append(a[1:k+1])
        check = sinh(k, n, a)
    return comps
def conv_list_to_str(list):
    str = ''
    for i in range(len(list)):
        str = str + list[i]
    return str
def brute_force(A = ['1','2','3','4','5','6','7','8','9'], kq = 100):
    lists = []
    for i in range(1,len(A)):
        lists.append(F(i))
    for list in lists:
        for li in list:
            comps = (tohop(True, len(li), len(A) - 1))
            for comp in comps:
                bt = A.copy()
                for idex,index_comp in enumerate(range(len(comp))):
                    bt.insert(comp[index_comp] + idex, li[index_comp])
                    gg = conv_list_to_str(bt)
                    if eval(gg) == kq:
                        print(gg +'='+ str(eval(gg)))



brute_force()

