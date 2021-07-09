#happy number
n=int(input("Enter Number:"))
while(n!=1 and n!=4):
	ss=0
	while(n):
		r=n%10
		ss+=r**2
		n//=10
	n=ss
if (n==1):
	print("happy")
else:
	print("unhappy")