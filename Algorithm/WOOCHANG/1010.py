# DP를 이용하였다. 이때 left와 right가 같을때에는 경우에 수가 1이고 left는 right보다 클 수 없습니다다.
# 또 result[left][right]는 이전의 값들을 더하는 방식이므로 다음과 같은 규칙이 있습니다.
# result[left][right] = result[left][right-1] + result[left-1][right-1] <- 이 부분은 left, right가 각각 1~5의 값을 가질때 손을로 직접해보면서 규칙을 찾았습니다.

num_case = int(input()) 

result = [[0 for _ in range(31)] for _ in range(31)] 

for left in range(1,31):
    for right in range(1,31):
        if left > right:
            continue

        if left == 1:
            if right == 1:
                result[left][right] = 1
            else:
                result[left][right] = right
        else:
            if left == right:
                result[left][right] = 1
            else:
                result[left][right] = result[left][right-1] + result[left-1][right-1]


for _ in range(num_case):
    left, right = map(int, input().split())

    print(result[left][right])
