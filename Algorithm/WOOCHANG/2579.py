import sys

input = sys.stdin.readline
n = int(input())
step_list = [int(input()) for _ in range(n)]
r_step_list = step_list[::-1]
count = 1
dp_table = [step_list[0]]

def solve(current, index, count):
    if current >= n-1:
        if current == n-1 and count != 3:
            return dp_table.append(dp_table[index] + r_step_list[current])
        else:
            return
    if count != 3:
        if dp_table[index] + r_step_list[current] > dp_table[index] + r_step_list[current+1]:
            dp_table.append(dp_table[index] + r_step_list[current])
            solve(current+1, index+1, count+1)
        else:
            dp_table.append(dp_table[index] + r_step_list[current+1])
            solve(current+2, index+1, 1)
    else:
        dp_table.append(dp_table[index] + r_step_list[current+1])
        solve(current+2, index+1, 1)

solve(1,0, 1)
print(dp_table[-1])