divList = []
while (1):
    num = int(input())
    if num ==-1:
        break

    for i in range(1, num):
        if num % i == 0:
            divList.append(i)
    if sum(divList) == num:
        print(f'{num} = 1', end = '')
        for n in range(1, len(divList)):
            print(f' + {divList[n]}', end = '')
        print()
        divList.clear()
        
    else : 
        print( f'{num} is NOT perfect.')
        divList.clear()