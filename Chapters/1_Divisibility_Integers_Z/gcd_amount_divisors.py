# Python Program to find the amount of
# Divisors of Two Numbers

#a = 12
#b = 24

a = int(input("1st:  "))
b = int(input("2nd:  "))

n = 0

for i in range(1, min(a, b)+1):
	if a%i==b%i==0:
		n+=1
	
if __name__ == "__main__":
	print(n)