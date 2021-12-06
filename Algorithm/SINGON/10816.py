import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

dic = dict() #사전식 배열

for i in A:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in range(m):
    if B[i] in dic:
        print(dic[B[i]], end = ' ')
    else:
        print(0, end = ' ')
