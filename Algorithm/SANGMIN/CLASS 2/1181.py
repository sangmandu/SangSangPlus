'''
https://www.acmicpc.net/problem/1181
단어 정렬
[풀이]
'''
import sys
input = sys.stdin.readline

n = int(input())
vocab = sorted(list(set([input().strip() for _ in range(n)])), key=lambda x : (len(x), x))
print(*vocab, sep='\n')






