cur_hour, cur_min  = map(int, input().split())
cookingMin = int(input())

fin_min = (cur_min + cookingMin)%60
fin_hour = ((cur_min + cookingMin)//60 + cur_hour) % 24

print(f'{fin_hour} {fin_min}')