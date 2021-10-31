import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)
ans = 0
while start <= end:
    mid = (start+end)//2
    height = sum(tree-mid if tree-mid>0 else 0 for tree in trees)
    if height < m:
        end = mid - 1
    elif height >= m:
        ans = mid
        start = mid + 1
print(ans)
