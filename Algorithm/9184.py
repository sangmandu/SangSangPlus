'''
https://www.acmicpc.net/problem/9184
신나는 함수 실행
[풀이]
1. dictionary를 사용해서 매번 계산한 값을 기억해둔다.
'''
import sys
input = sys.stdin.readline
dic = {}

def w(a, b ,c):
    if (a, b, c) in dic.keys():
        return dic[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        dic[(a, b, c)] = 1
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b and b < c:
        dic[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dic[(a, b, c)]
    dic[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dic[(a, b, c)]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
    
