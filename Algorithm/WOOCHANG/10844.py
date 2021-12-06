'''
i번째의 값은 좌우의 i-1번째 값의 함이므로 다음과 같이 구하면 된다.
'''
n = int(input())

dp_table = [[1 if i != 0 and j == 0 else 0 for j in range(n)] for i in range(10)]

if n != 1:
    dp_table[0][0] = 1
    for i in range(1,n):
        for j in range(10):
            if j != 9 and j != 0:
                dp_table[j][i] = dp_table[j-1][i-1] + dp_table[j+1][i-1]
            elif j == 0 :
                dp_table[j][i] = dp_table[j+1][i-1]
            else:
                dp_table[j][i] = dp_table[j-1][i-1]

print(sum([dp_table[i][-1] for i in range(10) if i != 0])%1000000000)