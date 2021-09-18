import sys
N = int(sys.stdin.readline())
Expected = []
for _ in range(1, N+1):
    A = int(sys.stdin.readline())
    Expected.append(A)
Expected.sort()
Answer = 0
for num in range(1,N+1):
    Answer += abs(num-Expected[num-1])
print(Answer)
