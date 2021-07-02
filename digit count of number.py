#digit count of number
n=int(input("Enter number:"))
c=0
while(n):
	r=n%10
	c+=1
	n//=10
print(c)