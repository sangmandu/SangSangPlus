import sys
def solution(N, Value):
    Benefit = 0
    target = Value[0] #마지막 날 주가를 그 날에 있는 주식을 팔 초기 기준으로 잡음
    for i in range(1, N):
        if Value[i]>= target: #마지막 날 주가보다 주가가 큰 날이 있으면
            target = Value[i] # 그 날에 주식을 파는 날로 잡음
        else:
            Benefit += target-Value[i] #아니면 target날짜에 주식을 팔아 이익을 챙김
    print(Benefit)

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    Value = list(map(int,sys.stdin.readline().split()))
    Value.reverse() #마지막 날 주가부터 정렬하면서 이익을 계산할 계획
    solution(N, Value)
