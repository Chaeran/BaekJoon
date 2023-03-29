list = []
max = 0
for i in range(9):
    list.append(int(input()))
    if max < list[i]:
        max = list[i]
        order = i+1

print(max)
print(order)