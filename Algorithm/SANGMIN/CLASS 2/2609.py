'''
https://www.acmicpc.net/problem/2609
최대공약수와 최소공배수
[풀이]
'''
import sys
input = sys.stdin.readline

import math
n, m = map(int, input().split())
print(math.gcd(n, m), math.lcm(n, m), sep='\n')
