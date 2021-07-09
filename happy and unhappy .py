#happy number
n=int(input("Enter Number:"))
while(n>9):
	ss=0
	while(n):
		r=n%10
		ss+=r**2
		n//=10
	n=ss
if (n==1 or n==7):
	print("happy")
else:
	print("unhappy")