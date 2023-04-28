#mat = [[0 for _ in range(101)] 0 for _ in range(101)]# 2차원 배열 선언
mat = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())# 색종이의 수
for _ in range(n):
    w, h = map(int, input().split())# 색종이 붙이기
    for i in range(w, w+10):
        for j in range(h, h+10):
            mat[i][j] = 1
answer = 0
for row in mat:
    answer+= row.count(1)
print(answer)
#print(sum(mat))