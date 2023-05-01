div, th = map(int, input().split()) #수, 번째 입력받기
n = 0
for i in range(1, div+1):
    if div % i == 0 :
        n += 1
        if n == th : 
            print(i)
            break
        elif div == i : 
            print("0")