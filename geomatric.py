import math
def prob(n, p):
    return pow((1 - p),(n-1))*p

def infoMeasure(n, p):
    return -math.log(prob(n, p), 2)

def sumProb(N, p):
    """
    Chứng minh tổng xác suất của phân bố geometric bằng 1, cho N = 5000 và p = 0.5. 
    """
    sum = 0 
    for i in range(1, N + 1):
        sum += prob(i, p)

    return sum

def approxEntropy(N, p):
    """
    Lấy N = 10000 và p = 0.5.
    """
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p)*infoMeasure(i, p)
    return sum

approxEntropy(10000, 0.5)