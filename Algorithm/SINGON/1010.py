import math

def choice(N, M):
    return math.factorial(M)/(math.factorial(N)*math.factorial(M-N))
print(choice(13,29))
