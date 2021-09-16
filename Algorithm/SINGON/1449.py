import sys
num, length = map(int,input().split())
holes = list(map(int,input().split()))
holes.sort()
"""물이 새는 곳은 가장 왼쪽에서 정수만큼 떨어진 거리이고 (x-0.5,x+0.5)만큼 테이프를 쓰므로
겹쳐지지 않으며 각 구멍을 막는데 필요한 길이는 1이다.
따라서 필요한 테이프 개수는 구멍개수를 테이프 한 개당 길이로 나눈 수에서 소수 첫째자리에서 올림을 하면 된다."""
if num%length ==0:
    print(num/length)
else:
    print(int(num//length)+1)
