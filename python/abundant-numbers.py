for i in range(1,201):
	if sum([j for j in range(1,i) if i%j==0])>i:print(i)
