a = int(input())
b = list(map(int, input().split()))
print(sum(b) / max(b) * 100 / a)  
