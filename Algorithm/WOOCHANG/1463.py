'''
인덱스 중에서 3의 제곱들과 2의 제곱들은 for문을 돌면서 i 값을 할당해주었고(에를 들어서 8은 2의 3승이므로 3을 할당) 나머지 인덱스는 3으로 나눠지면
dp_table[index//3]의 값에 + 1을 해줬고 (index-1)이 3으로 나눠지면 dp_table[(index-1)//3]의 값에 +1을 해주었고
이 두개에 해당하지 않는 인덱스는 dp_table[index//2] +1로 값을 넣어줬습니다.

그리고 위와 같은 과정을 제곱근 n + 1만큼 수행하도록 하므로
'''
import sys

input = sys.stdin.readline

n = int(input())
dp_table = [0 for i in range(n+1)]
dp_table[1] = 1

for i in range(1, int(n**1/2)+1):
    if n >= 3**i:
        dp_table[3**i] += i

    if n >= 2**i:
        dp_table[2**i] += i

    if dp_table[i] == 0:
        if i % 3 == 0:
            dp_table[i] = dp_table[i//3] + 1
        elif (i-1) % 3 == 0:
            dp_table[i] = dp_table[(i-1)//3] + 1
        else:
            dp_table[i] = dp_table[i//2] + 1

def solve(index):
    if dp_table[index] != 0:
        return dp_table[index]
    else:
        return min(dp_table[index//3]+1, dp_table[index//2]+1)

print(solve(n))
