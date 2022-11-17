// C++ code to verify Vantieghem's Theorem
#include <bits/stdc++.h>
using namespace std;

void checkVantieghemsTheorem(int limit)
{
	long long unsigned prod = 1;
	for (long long unsigned n = 2; n < limit; n++) {

		// Check if above condition is satisfied
		if (((prod - n) % ((1LL << n) - 1)) == 0)
			cout << n << " is prime\n";

		// product of previous powers of 2
		prod *= ((1LL << n) - 1);
	}
}

// Driver code
int main()
{
	checkVantieghemsTheorem(10);
	return 0;
}