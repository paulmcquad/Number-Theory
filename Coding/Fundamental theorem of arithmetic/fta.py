# Description: Print all the prime factors of a given number.
# Author     : Paul McQuade <paulmcquad@gmail.com>
# License    : GPLv3

def main():
    print("Type in No. to factor:")	
    n = int(input())
    i = 2
    out = ""
	
    while not 1 == n:
        
        fm = 0
        while n % i == 0:
            fm += 1
            n /= i
		
        if fm:
            out += str(i) + "^" + str(fm) + "*"
        i += 1

    print(out[:-1])	  

main()