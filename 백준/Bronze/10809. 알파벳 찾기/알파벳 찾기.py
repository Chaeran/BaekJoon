word = input()    #단어 입력받기
posList = []
for x in range(97,123):    #아스키 코드 사용
	pos = word.find(chr(x))    # find함수 : 문자열에서 해당 문자의 위치 알려줌. 없으면 -1
	posList.append(pos)
print(*posList)