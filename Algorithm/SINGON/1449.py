"""정석적 풀이는 아니지만 이것이 더 빠를 것 같았다는 것을 생각해서 이 풀이로 올립니다.
서로 겹치지 않기 때문에 이 풀이가 가능하다고 생각합니다"""
import sys
num, length = map(int,sys.stdin.readline().split())
holes = list(map(int,sys.stdin.readline().split()))
holes.sort()
"""물이 새는 곳은 가장 왼쪽에서 정수만큼 떨어진 거리이고 (x-0.5,x+0.5)만큼 테이프를 쓰므로
겹쳐지지 않으며 각 구멍을 막는데 필요한 길이는 1이다.
따라서 필요한 테이프 개수는 구멍개수를 테이프 한 개당 길이로 나눈 수에서 소수 첫째자리에서 올림을 하면 된다."""
if num%length ==0:
    print(num/length)
else:
    print(int(num//length)+1)
