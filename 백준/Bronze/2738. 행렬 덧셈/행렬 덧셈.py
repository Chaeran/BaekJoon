n,m = map(int, input().split())#행n, 렬m : 입력받기
matrix1 = []
matrix2 = []
for i in range(n):
	row = list(map(int, input().split()))
	matrix1.append(row)
for i in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)
for i in range(n):
	for j in range(m):
		matrix1[i][j] = matrix1[i][j] + matrix2[i][j]
	print(*matrix1[i])