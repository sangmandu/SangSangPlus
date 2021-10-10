import sys
input = sys.stdin.readline
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            A[i][j] += A[i-1][j]
        elif j == i :
            A[i][j] += A[i-1][j-1]
        else:
            A[i][j] += max(A[i-1][j-1], A[i-1][j])
print(max(A[n-1]))
