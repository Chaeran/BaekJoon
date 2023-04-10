import sys
T = int(input())
for _ in range(T):
	a,b = sys.stdin.readline().split()
	a = int(a)
	for i in range(len(b)):
		print(b[i]*a, end="")
	print()