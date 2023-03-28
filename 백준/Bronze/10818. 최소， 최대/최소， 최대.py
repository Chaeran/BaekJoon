n = int(input())
list = list(map(int, input().split()))
min = list[0]
max = list[0]
for i in range(1, n):
    if min > list[i] : 
	    min = list[i]
    if max < list[i]:
    	max = list[i]

print(min, max)