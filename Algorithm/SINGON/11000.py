import sys
import heapq # heapq를 써야지 빠르다.
input = sys.stdin.readline
N = int(input())
timetable = [tuple(map(int, input().split())) for _ in range(N)]
timetable.sort(key = lambda x : x[0])
queue = []
heapq.heappush(queue, timetable[0][1])
del timetable[0]
for lesson in timetable:
    if queue[0] <= lesson[0]:
        heapq.heappop(queue)
    heapq.heappush(queue, lesson[1])
print(len(queue))
