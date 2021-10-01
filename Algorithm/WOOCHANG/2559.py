'''
연속된 합은 시작지점부터 k까지의 합이다.
이때 현재 연속 합은 이전 index의 연속합에서 해당 값(temperature_list[이전 index])를 빼주고 현재 값(temperature_list[현재 index])를 더해주면 된다.
'''
import sys

input = sys.stdin.readline

def solve(n, k):
    temperature_list = list(map(int, input().split()))
    df_list = [0 for _ in range(n-k+1)]
    heap_list = []
    if n == k:
        print(sum(temperature_list))
    else:
        if k != 1:
            for start in range(n-k+1):
                if start == 0:
                    df_list[start] = sum(temperature_list[start:start+k])
                else:
                    df_list[start] = df_list[start-1] - temperature_list[start-1] + temperature_list[start+k-1]
            df_list.sort(reverse=True)
            print(df_list[0])
        else:
            temperature_list.sort(reverse=True)
            print(temperature_list[0])


if __name__ == "__main__":
    n, k = map(int, input().split())
    solve(n, k)
