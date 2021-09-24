s = int(input())
for grade, cut in zip(["A", "B", "C", "D", "F"], [90, 80, 70, 60, 0]):
    if s >= cut:
        print(grade)
        break
