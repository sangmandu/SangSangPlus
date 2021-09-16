import math
import sys
def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

def choice(N, M):
    return factorial(M)//(factorial(N)*factorial(M-N)) # //가 아닌 /를 사용하면 .0 이 나와 틀렸다고 뜸!
T = int(input())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(choice(N,M))
