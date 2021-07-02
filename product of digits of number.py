n=int(input("enter number:"))
p=1
while(n):
	r=n%10
	p*=r
	n=n//10
print(p)