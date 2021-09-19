import sys
input = sys.stdin.readline
N = int(input())
schedules = [] # 시간 스케줄을 모두 넣을 것임
for _ in range(N):
    start, end = map(int, input().split())
    schedule = (start, end)
    schedules.append(schedule)
schedules.sort(key = lambda x: (x[1], x[0])) #끝나는 시간이 빠른순, 같을 시 차선으로 시작하는 시간이 빠른 순으로 정함.
end_time = schedules[0][1] # 초기 하나의 기준을 잡음.
cnt =1 #스케줄 하나가 잡혀있으므로
for i in range(1, N):
    if schedules[i][0] >= end_time:
        cnt +=1
        end_time = schedules[i][1]
print(cnt)


