def gcd(n1,n2):
    gcd=1
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            gcd=i
        return gcd
def LCM(n1, n2):
        for i in range(max(n1, n2), n1*n2 + 1):
            if i % n1 == 0 and i % n2 == 0:
                return i
            
print(LCM(5,9),gcd(5,9))
