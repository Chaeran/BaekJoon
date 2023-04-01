numList  = []
for _ in range(28):
    a = int(input())
    numList.append(a)
    numList.sort()
for i in range(1,31):
    if i not in numList:
        print(i)