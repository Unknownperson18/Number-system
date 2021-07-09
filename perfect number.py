#perfect number
n=int(input("Enter number:"))
d=n
s=0
for i in range(1,n//2+1):
	if(n%i==0):
		print("factors of ",d,"=",i)
		print(s,"+",i,"=",s+i)
		s+=i
if(s==n):
	print(d,"perfect number")
else:
	print(d,"is not a perfect number")