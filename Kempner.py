def Kempner(Nmax):
    K = 0.0
    for n in range(1,Nmax+1):
        num=str(n)
        if "9" in num:
            continue
        K = K + 1./n
    return (K)
A=Kempner(1000000)
print (A)