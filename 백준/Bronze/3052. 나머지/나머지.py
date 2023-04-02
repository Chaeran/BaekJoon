remains = []
for _ in range(10):
    a = int(input())%42
    remains.append(a)
    
remains.sort()

n = 1
for i in range(0,9):
    if remains[i] != remains[i+1]:
        n+=1
print(n)