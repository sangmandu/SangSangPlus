'''
https://www.acmicpc.net/problem/1904
01타일
[풀이]
1. 피보나치 방법으로 푼다.
'''
import sys
input = sys.stdin.readline

a, b = 1, 1
for _ in range(int(input())):
    a, b = b, (a+b) % 15746
print(a)
'''
n = 1 | 1 1
n = 2 | 11 2 2
n = 3 | 111 12 21 3
n = 4 | 1111 112 121 211 22 5
n = 5 | 11111 2111 1211 1121 1112 212 122 221 8
n = 6 | 111111 21111 12111 11211 11121 11112 2112 2121 2211 222
'''
