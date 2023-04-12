numbers = input()#문자열 입력 받기
numList = list(numbers)#처리를 위해 리스트로 바꿔주기
numList.reverse()#리스트 순서 거꾸로
numbers = ''.join(numList) #리스트의 원소들을 문자열로 합치기
a,b = map(int, numbers.split())#split() -> a,b
print(max(a,b))#출력 max(a,b)