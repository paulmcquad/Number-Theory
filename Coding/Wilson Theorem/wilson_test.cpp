// C++ implementation to check if a number is
// prime or not using Wilson Primality Test
#include <bits/stdc++.h>
using namespace std;

// Function to calculate the factorial
long fact(const int& p)
{
	if (p <= 1)
		return 1;
	return p * fact(p - 1);
}

// Function to check if the
// number is prime or not
bool isPrime(const int& p)
{
	if (p == 4)
		return false;
	return bool(fact(p >> 1) % p);
}

int main()
{
	int n = 0;
	cin >> n;
	cout << isPrime(n) << endl;
	return 0;
}
