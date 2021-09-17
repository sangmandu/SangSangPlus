'''
https://www.acmicpc.net/problem/1449
수리공 항승
[풀이]
1. 누수된 위치 받기
2. 테이프가 붙여지는 왼쪽 인덱스 jdx
=> 새로운 테이프가 붙여질 때 마다 jdx=idx 로 고정된다
3. 테이프가 붙여지는 오른쪽 인덱스 idx
=> 테이프를 붙일 수 있으면 +1씩 증가한다.
'''
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
leak = sorted(list(map(int, input().split())))
idx = jdx = 0
answer = 1
while idx < len(leak)-1:
    idx += 1
    if leak[idx]-leak[jdx] <= L-1:
        continue
    jdx = idx
    answer += 1
print(answer)
