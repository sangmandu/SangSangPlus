'''
https://www.acmicpc.net/problem/1932
정수 삼각형
[풀이]
1. 첫 원소는 항상 이전의 첫 원소와 더해진다.
2. 마지막 원소는 항상 이전의 마지막 원소와 더해진다.
3. 나머지 원소는 이전의 두 원소 중 더 큰 원소와 더해진다.
=> 이 때, i번째에 있는 현재의 원소에 대해 이전의 원소는 i번째와 i-1번째이다.
'''
import sys
input = sys.stdin.readline

n = int(input())
pre = [int(input())]
for i in range(1, n):
    lst = list(map(int, input().split()))
    pre = [pre[0]+lst[0]] + [lst[idx] + max(pre[idx-1], pre[idx]) for idx in range(1, i)] + [pre[-1]+lst[-1]]
print(max(pre))
