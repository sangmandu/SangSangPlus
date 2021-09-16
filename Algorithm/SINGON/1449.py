import sys
num, length = map(int,sys.stdin.readline().split())
holes = list(map(int,sys.stdin.readline().split()))
holes.sort()
"""물이 새는 곳은 가장 왼쪽에서 정수만큼 떨어진 거리이고 (x-0.5,x+0.5)만큼 테이프를 쓰므로
겹쳐지지 않으며 각 구멍을 막는데 필요한 길이는 1이다.
따라서 필요한 테이프 개수는 구멍개수를 테이프 한 개당 길이로 나눈 수에서 소수 첫째자리에서 올림을 하면 된다."""
# 수정 - 테이프를 자를 수 없으므로 위와 같은 생각은 필요없고 정렬을 이용해서 풀 수 밖에 없다는 생각이 들었다.
cnt = 0
st = 0
for hole in holes:
    if st < hole :
        cnt += 1
        st = hole + length -1
print(cnt)
