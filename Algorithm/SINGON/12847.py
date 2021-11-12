import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split())) #1일부터 n일 까지 일급 T(i)가 순서대로 주어짐
step = m
target = sum(numbers[:step]) #m일 일해서 얻은 이익
answer = target
for i in range(step, n):
    target += numbers[i] - numbers[i-step]
    answer = max(answer, target) #최대 이익 찾기
print(answer)
