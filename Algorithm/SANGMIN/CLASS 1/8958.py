t = int(input())
for _ in range(t):
    answer = tmp = 0
    for s in input():
        if s == "O":
            answer += 1 + tmp
            tmp += 1
            continue
        tmp = 0
    print(answer)
