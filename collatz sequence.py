n=int(input("Enter anumber:"))
print(n)
c=0
while(n!=1):
	if(n%2==0):
		print(n,"is even so number=",n/2)
		n=n/2
	else:
		print(n,"is odd so number= ",3*n+1)
		n=3*n+1
	c+=1
print(n)
print("Number of steps to reach 1 =",c)