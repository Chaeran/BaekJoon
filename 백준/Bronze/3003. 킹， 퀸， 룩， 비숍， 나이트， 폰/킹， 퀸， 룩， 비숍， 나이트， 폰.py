ChList = [1, 1, 2, 2, 2, 8]
myList = list(map(int, input().split()))
for i in range(6):
	print(ChList[i]-myList[i], end=' ')