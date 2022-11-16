// CPP program to check
// Chen prime number

// Chen Prime number
// A109611 - Chen primes: primes p such that p + 2 is either a prime or a semiprime.

#include <bits/stdc++.h>
using namespace std;

// Utility function to check whether
// number is semiprime or not
int isSemiprime(int num)
{
	int cnt = 0;

	for (int i = 2; cnt < 2 && i * i <= num; ++i)
		while (num % i == 0)
			num /= i, ++cnt; // Increment count
	// of prime numbers

	// If number is greater than 1, add it to
	// the count variable as it indicates the
	// number remain is prime number
	if (num > 1)
		++cnt;

	// Return '1' if count is equal to '2' else
	// return '0'
	return cnt == 2;
}

// Utility function to check whether
// the given number is prime or not
bool isPrime(int n)
{
	// Corner cases
	if (n <= 1)
		return false;
	if (n <= 3)
		return true;

	// This is checked so that we can skip
	// middle five numbers in below loop
	if (n % 2 == 0 || n % 3 == 0)
		return false;

	for (int i = 5; i * i <= n; i = i + 6) {
		if (n % i == 0 || n % (i + 2) == 0) {
			return false;
		}
	}

	return true;
}

// Function to check Chen prime number
bool isChenPrime(int n)
{

	if (isPrime(n) && (isSemiprime(n + 2) || isPrime(n + 2)))
		return true;
	else
		return false;
}

// Driver code
int main()
{
	int n = 0;
	cin >> n;

	if (isChenPrime(n))
		cout << "YES\n";
	else
		cout << "NO\n";

	return 0;
}
