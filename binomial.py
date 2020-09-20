import math
def giaiThua(n):
    i = 0
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result

def prob(n, p, N):
    return (giaiThua(N))/((pow(p,n))*giaiThua(n)*giaiThua(N-n))

def infoMeasure(n, p, N):
    return -math.log(prob(n, p, N), 2)

def sumProb(N, p):
    sum = 0 
    for i in range(1, N + 1):
        sum += prob(i, p, N)

    return sum

def approxEntropy(N, p):
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, N)*infoMeasure(i, p, N)
    return sum
