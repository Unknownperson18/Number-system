#sum of even digits and odd digits in number
n=int(input("select Number:"))
t=n
e_sum=0
o_sum=0
e_count=0
o_count=0
while(n):
	r=n%10
	if(r%2==0):
		e_sum+=r
		e_count+=1
	else:
		o_sum+=r
		o_count+=1
	n//=10
print(e_count,"even digits and",o_count,"odd digits in",t)
print("even digits sum:",e_sum)
print("odd digits sum:",o_sum)