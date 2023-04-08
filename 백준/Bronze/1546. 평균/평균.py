import sys
M = int(input()) #입력될 개수
scores = list(map(int, sys.stdin.readline().split()))
max = max(scores)
for i in range(M):
	 scores[i] = scores[i]/max * 100
print(sum(scores)/M)