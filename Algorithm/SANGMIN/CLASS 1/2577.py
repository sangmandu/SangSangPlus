a, b, c = [int(input()) for _ in range(3)]
d = str(a*b*c)
for i in range(10):
    print(d.count(str(i)))
