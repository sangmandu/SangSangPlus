import sys
 
n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
ans = 0

for i in range(1, m-1):
    for j in range(i+1, m):
        s1 = sum([table[a][b] for a in range(n) for b in range(i)])
        s2 = sum([table[a][b] for a in range(n) for b in range(i, j)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)

for i in range(1, m):
    for j in range(1, n):
        s1 = sum([table[a][b] for a in range(j) for b in range(i)])
        s2 = sum([table[a][b] for a in range(j) for b in range(i, m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        ans = max(ans, s1*s2*s3)

for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)

for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(j)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)

for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(j, m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j)])
        ans = max(ans, s1*s2*s3)
 
for i in range(1, n-1):
    for j in range(i+1, n):
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, j) for b in range(m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        ans = max(ans, s1*s2*s3)
 
print(ans)