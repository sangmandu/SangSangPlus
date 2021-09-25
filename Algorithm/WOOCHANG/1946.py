'''
조건대로 서류, 면접 둘 다 다른 지원자보다 떨어지는 사람을 count하지 않기 위해서
먼저 score1(서류)을 기준으로 정렬을 하고 순서대로 조건을 비교한다.
이때 score1을 기준으로 정렬하였으므로 score[0]의 서류 점수는 최상이므로
score2를 계속 비교하고 더 낮은 score2로 갱신해주면 된다.
이때 score1을 기준으로 정렬해주었으므로 나중에 갱신된 socre2보다 그 전에 score2가 높더라도 score1이 낮으므로 조건은
만족시킨다.
'''
import sys

input = sys.stdin.readline

def solve(test_case):
    for _ in range(test_case):
        n = int(input())
        score_list = [list(map(int, input().split())) for _ in range(n)]
        score_list.sort()
        top_score_1, top_score_2 = score_list[0]
        count = 1
        for score_1, score_2 in score_list[1:]:
            if score_2 == 1:
                count += 1
                break
            if score_2 < top_score_2:
                count += 1
                top_score_2 = score_2
        print(count)

if __name__ == '__main__':
    test_case = int(input())
    solve(test_case)

