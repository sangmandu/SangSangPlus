import sys
from itertools import accumulate
def solution(N,M):
    # A = list(list(map(int, input().split())) for _ in range(N))
    B = [[0]*(N+1)]
    for _ in range(N):
        B.append([0]+list(accumulate(map(int,input().split()))))
    for j in range(1, N+1):
        for i in range(1,N):
            B[i+1][j] += B[i][j]
    for _ in range(M):
        x1, y1, x2, y2 = map(int,input().split())
        print(B[x2][y2]-B[x1-1][y2]-B[x2][y1-1]+B[x1-1][y1-1])
        
if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    solution(N,M)
