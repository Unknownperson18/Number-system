#sum of digits of number
n=int(input("Enter number:"))
s=0
while(n):
	r=n%10
	print(s,"+",r,"+",s+r)
	s+=r
	n=n//10
print(s)