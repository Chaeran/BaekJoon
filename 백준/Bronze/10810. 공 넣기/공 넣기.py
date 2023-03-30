N, M = map(int, input().split())
list = [0 for i in range(N)]
for a in range (M):
    i, j, k = map(int, input().split())
    for b in range(i-1, j):
        list[b] = k
print(*list)