import math
def giaiThua(n):
    i = 0
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result

def prob(n, p, N, r):
    return (giaiThua(n))/((pow(p,n))*giaiThua(n-r+1)*giaiThua(r-1))

def infoMeasure(n, p, N, r):
    return -math.log(prob(n,p,N,r),2)

def sumProb(N, p, r):
    sum = 0 
    for i in range(1, N + 1):
        sum += prob(i, p, N, r)

    return sum

def approxEntropy(N, p, r):
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, N, r)*infoMeasure(i, p, N, r)
    return sum