N, M = map(int, input().split())
list = []
for a in range(N):
	list.append(a+1)
for _ in range(M):
	i, j = map(int, input().split())
	temp = list[i-1]
	list[i-1] = list[j-1]
	list[j-1] = temp
print(*list)