n,B = input().split()
B = int(B)
nList = list(n)
num = 0
for i in range(len(nList)) : 
	if ord(nList[i]) < 58 : # 아스키 코드가 57보다 작으면 숫자
		nList[i] = int(nList[i])
	else:
		nList[i] = ord(nList[i])-55
		
	num += (B**(len(nList)-(i+1))) * nList[i]

print(num)
