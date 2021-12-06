import sys
input = sys.stdin.readline

n = int(input())
answer = cnt = 1
while n > cnt:
    cnt += 6 * answer
    answer += 1
print(answer)
