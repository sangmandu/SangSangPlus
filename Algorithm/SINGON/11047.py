import sys
input = sys.stdin.readline
N, K = map(int, input().split())
cnt = 0
A = []
for _ in range(N):
    X = int(input())
    A.append(X)
A.sort(reverse = True)
for i in A:
    Y = K//i
    K -= Y*i
    cnt +=Y
    if K == 0:
        break
print(cnt)
