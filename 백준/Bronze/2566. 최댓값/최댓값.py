mat = []
maxList = []
for _ in range(9): 
    row = list(map(int, input().split()))    #9개 입력 - 리스트화
    mat.append(row)    #matrix에 행 append
    maxList.append(max(row)) #행중 가장 큰 것 list에 저장
     
max = max(maxList) #max list 중 가장 큰 것 찾기
r = maxList.index(max) # 인덱스 반환 - 행
c = mat[r].index(max) #matrix에서 해당 행으로 가서 max 찾고 인덱스 반환 - 열
print(max)
print(r+1, c+1)