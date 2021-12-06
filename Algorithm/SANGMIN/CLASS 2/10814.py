'''
https://www.acmicpc.net/problem/10814
나이순 정렬
[풀이]
'''
import sys
input = sys.stdin.readline

n = int(input())
users = [[i] + input().split() for i in range(n)]
print(*[' '.join([age, name]) for _, age, name in sorted(users, key=lambda x: (int(x[1]), x[0]))], sep='\n')
