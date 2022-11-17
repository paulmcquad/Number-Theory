# Python3 implementation as a
# proof of the Midy's theorem

# Returns repeating sequence of a fraction.
# If repeating sequence doesn't exits,
# then returns -1
def fractionToDecimal(numerator, denominator):
	res = ""

	''' Create a map to store already seen remainders
	remainder is used as key and its position in
	result is stored as value. Note that we need
	position for cases like 1/6. In this case,
	the recurring sequence doesn't start from first
	remainder. '''
	mp = dict()

	# Find first remainder
	rem = numerator % denominator

	# Keep finding remainder until either remainder
	# becomes 0 or repeats
	while ((rem != 0) and (rem not in mp)):

		# Store this remainder
		mp[rem] = len(res)

		# Multiply remainder with 10
		rem = rem * 10

		# Append rem / denr to result
		res_part = (rem // denominator)
		res += str(res_part)

		# Update remainder
		rem = rem % denominator

	return ["-1", res[mp[rem]:]][rem != 0]


# Checks whether a number is prime or not
def isPrime(n):
	for i in range(2, 1 + n // 2):
		if (n % i == 0):
			return False
	return True


# If all conditions are met,
# it proves Midy's theorem
def Midys(str, n):

	l = len(str)
	part1 = 0
	part2 = 0
	if (not isPrime(n)):
		print("Denominator is not prime, thus Midy's theorem is not applicable")

	elif (l % 2 == 0):

		for i in range(l // 2):

			part1 = part1 * 10 + int(str[i])
			part2 = part2 * 10 + int(str[(l // 2) + i])

		print(part1, "+", part2, "=", (part1 + part2))
		print("Midy's theorem holds!")

	else:

		print(
			"The repeating decimal is of odd length thus Midy's theorem is not applicable")


# Driver code
#numr = 2
#denr = 11

#numr = 1
#denr = 7

numr = int(input())
denr = int(input())


res = fractionToDecimal(numr, denr)
if (res == "-1"):
	print("The fraction does not have repeating decimal")

else:
	print("Repeating decimal =", res)
	Midys(res, denr)


# This code is contributed by phasing17.
