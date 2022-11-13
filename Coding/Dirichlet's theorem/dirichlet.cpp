// C++ implementation of
// the above approach
#include <bits/stdc++.h>
using namespace std;

// Utility function to check
// whether two numbers is
// co-prime or not
int coprime(int a, int b)
{
	if (__gcd(a, b) == 1)
		return true;
	else
		return false;
}

// Utility function to check
// whether a number is prime
// or not
bool isPrime(int n)
{
	// Corner case
	if (n <= 1)
		return false;

	if (n == 2 or n == 3)
		return true;

	// Check from 2 to sqrt(n)
	for (int i = 2; i * i <= n; i++)
		if (n % i == 0)
			return false;

	return true;
}

// finding the Prime numbers
void findNumbers(int a, int b, int n)
{

	bool possible = true;

	// Checking whether given
	// numbers are co-prime
	// or not
	if (!coprime(a, b))
		possible = false;

	int c1 = 1;
	int c2 = 1;

	int num1, num2;

	// To store the N primes
	set<int> st;
	// If 'possible' is true
	if (possible) {

		// Printing n numbers
		// of prime
		while ((int)st.size() != n) {

			// checking the form of a+nb
			num1 = a + (c1 * b);
			if (isPrime(num1)) {
				st.insert(num1);
			}
			c1++;

			// Checking the form of b+na
			num2 = b + (c2 * a);
			if (isPrime(num2)) {
				st.insert(num2);
			}
			c2++;
		}

		for (int i : st)
			cout << i << " ";
	}

	// If 'possible' is false
	// return -1
	else
		cout << "-1";
}

// Driver Code
int main()
{

	int a = 2;
	int b = 1;
	int n = 10;

	findNumbers(a, b, n);
	return 0;
}
