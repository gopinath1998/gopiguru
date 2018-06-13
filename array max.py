try:
	z=int(input())
	y=int(input())
	t=max(z,y)
	while(True):
		if (t%z==0 and t%y==0) :
			break
		t=t+1
	print(t)
except:
	print('invalid')
