import sys

input = sys.stdin.readline

def solve(n):
    rgb_price_list = [list(map(int, input().split())) for _ in range(n)]
    global n_house_price
    n_house_price = [0 for _ in range(n)]
    prev_color = None
    current_color = None
    min_price = None

    for index in range(n):
        min_price = min(rgb_price_list[index])
        current_color = rgb_price_list[index].index(min_price)

        if index == 0:
            prev_color = current_color
            n_house_price[index] = min_price
            continue

        if prev_color == current_color:
            if rgb_price_list[index][0] == rgb_price_list[index][1] == rgb_price_list[index][2]:
                n_house_price[index] = n_house_price[index - 1] + min_price
                prev_color = prev_color -1 if prev_color == 2 else prev_color + 1
            elif min_price == rgb_price_list[index][0] == rgb_price_list[index][1] or \
                min_price == rgb_price_list[index][0] == rgb_price_list[index][2] or \
                min_price == rgb_price_list[index][1] == rgb_price_list[index][2]:
                n_house_price[index] = n_house_price[index - 1] + min_price
                temp_list = [target for target in range(3) if target != prev_color]
                prev_color = temp_list[0] if rgb_price_list[index][prev_color[0]] == min_price else temp_list[1]
                continue
            other_list = [target for target in range(3) if rgb_price_list[index][target] != min_price]
            current_color = other_list[0] if rgb_price_list[index][other_list[0]] < rgb_price_list[index][other_list[1]] else other_list[1]
            min_price = rgb_price_list[index][current_color]
            n_house_price[index] = n_house_price[index-1] + min_price
            prev_color=current_color
        else:
            prev_color = current_color
            n_house_price[index] = n_house_price[index-1] + min_price


if __name__ == '__main__':
    n = int(input())
    solve(n)
    print(n_house_price[-1])