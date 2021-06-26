
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

def A(check:True,k,n):
    a = [0]
    list = []
    for i in range(1, n+1):
        a.append(i)
    while check:
        list.append(a[1:k+1])
        check = sinh(k,n,a)
    return list

print(A(True,1,8))