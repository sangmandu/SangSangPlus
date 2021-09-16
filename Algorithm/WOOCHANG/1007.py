'''
해결하지 못함;;;
각 점에 대한 경우를 재귀를 통해서 해결하려고 하였으나 search_min for문 안에서 어떻게 해야지 이전에
뽑은 index에 대한 정보를 다음 함수에 줘야할지 + 그러면서 험수 복귀 후에 append나 pop에 대한 원본 list의 값 손실? 등을 없앨 수 있는지 모르겠다;;;
'''
import math
import copy

test_case = int(input())

def vector_sum(point_pair_list):
    vector_list= []
    target_value = 0.0

    # 두 점에 대한 vector 계산
    for point_x, point_y in point_pair_list:
        temp_x = point_x[0] - point_y[0]
        temp_y = point_x[1] - point_y[1]
        vector_list.append((temp_x, temp_y))

    # vector에 대한 합 구하기
    for i in range(len(vector_list)):
        for j in range(i+1,len(vector_list)):
            x = vector_list[i][0] + vector_list[j][0]
            y = vector_list[i][1] + vector_list[j][1]
            target_value += math.sqrt(x**2 + y**2)

    return target_value





def search_min(point_list, point_pair_list, remain_num, min_value):
    if remain_num == 0:
        target_value = vector_sum(point_pair_list)
        return min(min_value,target_value)

    for i in range(remain_num-1):
        temp1 = point_list[i]
        for j in range(i+1, remain_num):
            temp2 = point_list[j]
            temp_pair_list = copy.deepcopy(point_pair_list)
            temp_pair_list.append((temp1, temp2))
            search_min(point_list, temp_pair_list, remain_num-2, min_value)




for _ in range(test_case):
    point_num = int(input())
    point_list = []
    for _ in range(point_num):
        point_list.append(list(map(int, input().split())))
