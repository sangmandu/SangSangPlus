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
