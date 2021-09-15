import math, sys, itertools

T = int(input())

for test_case in range(T):
    N = int(input()) # 점 (x, y)들 입력
    point = [] # 점들의 집합소
    total_x = 0 #점들 x의 합
    total_y = 0 #점들 y의 합

    for i in range(N):
        x, y = list(map(int,input().split(' ')))
        point.append([x, y])
        total_x += x
        total_y += y
    ret = sys.maxsize #최대 사이즈로 확장
    com = list(itertools.combinations(point, int(N/2))) #itertolls의 한 라이브러리인 combinations을 사용하여 point 점들중 N/2개 추출
    com_len = int(len(com)/2) #벡터는 두 점의 차이를 통해 만들어 지고 벡터의 합의 최소를 구하므로 절반의 점은 더하고 절반의 점은 빼서 x와 y의 제곱의 합의 루트를 구하면 된다.
    #떠라서 절반의 점을 추출하여 더할 것이다. 1팀을 더하고 2팀을 빼든 2팀을 더하고 1팀을 빼든 정답과 상관 없으므로 1팀은 더하고 2팀은 빼서 구하겠다.
    for element in com[:com_len]: #1팀에 있는 점 추출
        element = list(element)
        total_v1 = 0
        total_v2 = 0
        for v1, v2 in element:
            total_v1 += v1
            total_v2 += v2
        vx_total = total_x - total_v1 #2팀에 있는 x점의 합은 전체 x점의 합에서 1팀 x점의 합을 빼면 될 것이다.
        vy_total = total_y - total_v2 #2팀에 있는 y점의 합은 전체 y점의 합에서 1팀 y점의 합을 빼면 될 것이다.

        ret = min(ret, math.sqrt((total_v1-vx_total)**2 + (total_v1-vy_total)**2)) #최솟값 구하기.
    print(ret)
