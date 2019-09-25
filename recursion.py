def Hanoi(n,a,b,c):
	if n==1:
		print(a,'-->',c)
	else:
		Hanoi(n-1,a,c,b)
		Hanoi(1,a,b,c)
		Hanoi(n-1,b,a,c)

if __name__ == '__main__':
	Hanoi(5,"a","b","c")