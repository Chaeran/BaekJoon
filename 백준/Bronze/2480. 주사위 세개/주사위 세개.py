a = list(map(int, input().split()))

if a[0]==a[1] and a[1]==a[2]:
	reward = 10000+a[0]*1000
elif (a[0]==a[1] and a[1]!=a[2]) or (a[0]==a[2] and a[1]!=a[2]):
	reward = a[0]*100+ 1000 
elif (a[0]!=a[1] and a[1]==a[2]):
	reward = a[1]*100+ 1000 
else:
	reward = max(a)*100
print(reward)