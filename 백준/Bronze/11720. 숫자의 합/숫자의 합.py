n = int(input())
list=[]
words = input()
for i in range(n):
    list.append(int(words[i]))

sum = 0
for num in list:
    sum += num
print(sum)
