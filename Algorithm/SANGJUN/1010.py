from sys import stdin
from math import factorial
input = stdin.readline

# 오른쪽 사이트에서 왼쪽 사이트 수 만큼의 사이트만 선택하면 된다.
# 선택한다는 것 자체가 한 가지 경우의 수 이므로 한 가지 경우를 겹치지 않게 다리를 놓아준다고 생각하면 끝
def _1010(sites):
    N, M = sites
    return factorial(M) // (factorial(N) * factorial(M - N))

if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        print(_1010(map(int, input().split())))
