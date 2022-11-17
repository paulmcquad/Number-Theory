// CPP program to print all sophie germain
// prime number till n.
#include <bits/stdc++.h>
using namespace std;

// function to detect prime number
// here we have used sieve method
// https://www.geeksforgeeks.org/sieve-of-eratosthenes/
// to detect prime number
bool sieve(int n, bool prime[])
{
	for (int p = 2; p * p <= n; p++) {

		// If prime[p] is not changed, then
		// it is a prime
		if (prime[p] == true) {

			// Update all multiples of p
			for (int i = p * 2; i <= n; i += p)
				prime[i] = false;
		}
	}
}

int printSophieGermainNumber(int n)
{
	// We have made array till 2*n +1
	// so that we can check prime number
	// till that and conclude about sophie
	// germain prime .
	bool prime[2 * n + 1];
	memset(prime, true, sizeof(prime));
	sieve(2 * n + 1, prime);

	for (int i = 2; i <= n; ++i) {

		// checking every i whether it is
		// sophie germain prime or not.
		if (prime[i] && prime[2 * i + 1])
			cout << i << ", ";	
	}
}

int main()
{
    int n = 0;
    cin >> n;
	//int n = 25;
	printSophieGermainNumber(n);
	return 0;
}
