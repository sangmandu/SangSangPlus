n = int(input())
for i in range(max(1, n-len(str(n))*9), n):
    if i + sum([int(s) for s in str(i)]) == n:
        print(i)
        break
else:
    print(0)
        
    
