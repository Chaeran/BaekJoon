N,M = map(int, input().split())
basket = [a for a in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    for n in range((j-i)//2+1):
        basket[i+n-1],basket[j-n-1] = basket[j-n-1], basket[i+n-1]
print(*basket)