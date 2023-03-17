N, M = map(int, input().split())
min_D = 0x7FFFFFFF
sum = 0
num_list = list(map(int, input().split()))


for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            sum = num_list[i] + num_list[j] + num_list[k]
            if sum > M:
                continue
            if min_D > M - sum:
                min_D = M - sum
                result = sum
print(result)

