maxlen = 0
mat = []
for _ in range(5):
    row = list(input())
    mat.append(row)
    if len(row) > maxlen:
        maxlen = len(row)
for i in range(5):
	for _ in range(maxlen-len(mat[i])):
		mat[i].append('')
for j in range(maxlen):
	for i in range(5):
		print(mat[i][j], end='')