'''
시간초과때문에 여러 시도를 해서 겨우겨우 풀었습니다.
1. 처음에는 score_list과 result_list를 받아오는 부분을 for문으로 했는데 시간초과가 나왔습니다.
그래서 고민을 계속하다가 list comprehension에 함수를 넣을 수 있지 않을까 싶어서 score_list부분에 넣어봤고 다시 시도를 했습니다.
또 실패;;;
그래서 또 고민하다가 아! 삼항연산자도 list comprehension에 넣어줄 수 있을 것 같아서 코드를 고치고 시도를 했습니다.
2. score_list, result_list -> list comprehension으로 구현 -> 실패 ㅋ
3. sort, sorted함수를 사용하지 않고 수학적으로 접근해야 하겠구나 싶어서 -> 주어진 n명에게 n까지 등수를 받고 불만족이 최소값은 score_list의 합과 1~n등수까지의 합의 차를 구해주면
될 거라고 생각했지만 -> 실패, '틀렸습니다.'라고 나왔습니다 ㅠㅠ
4. 계속 삽질하고 어떻게 해야할까 고민하다가 우연히 sys.stdin.readline을 사용하면 I/O 성능이 빨라진다는 것을 알게 되어서 그렇게 고쳤더니 겨우 풀게 되었습니다. ㅎㅎ
총 걸린시간 1시간 30분정도이지만 오늘은 풀어서 기분이 좋습니다 ㅎㅎㅎㅎ
'''
import sys
n = int(sys.stdin.readline())
score_list =sorted([int(sys.stdin.readline()) for _ in range(n)])

enum_list = [i+1 for i in range(n)]
result_list = [abs(score-i) for i, score in zip(enum_list, score_list)]
print(sum(result_list))

# 이 부분은 위의 3번방식으로 해결하려고 한 코드입니다.
# score_list =[int(input()) for _ in range(n)]
# result = abs(sum(score_list) - sum(enum_list))
# print(result)


