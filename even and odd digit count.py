#Even digit count and odd digit count
n=int(input("Enter Number:"))
t=n
e_count=0
o_count=0
while(n):
	r=n%10
	if(r%2==0):
		e_count+=1
	else:
		o_count+=1
	n//=10
print("They are",e_count,"even numbers",o_count,"odd numbers in",t)