import sys
wordsList = []
while True:
    word = sys.stdin.readline().strip()
    if not word:
        break
    wordsList.append(word)#입력받을 때 엔터\n 기준으로 split 해 리스트에 넣기
for i in wordsList:
    print(i) #리스트 하나씩 출력 end = '\n'