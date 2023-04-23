letterList = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]#크로아티아 알파벳을 리스트에 넣어놓기
cnt = 0 # 문자 수
word = input()
for letter in letterList:
    if letter in word:
        word = word.replace(letter, "*")
cnt += len(word)
print(cnt)
