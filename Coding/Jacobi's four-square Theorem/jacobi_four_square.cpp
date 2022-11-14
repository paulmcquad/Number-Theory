// C++ implementation of above approach
#include <bits/stdc++.h>
using namespace std;

// Number of ways of writing n
// as a sum of 4 squares
int sum_of_4_squares(int n)
{
	// sum of odd and even factor
	int i, odd = 0, even = 0;

	// iterate from 1 to the number
	for (i = 1; i <= sqrt(n); i++) {
		// if i is the factor of n
		if (n % i == 0) {
			// if factor is even
			if (i % 2 == 0)
				even += i;

			// if factor is odd
			else
				odd += i;

			// n/i is also a factor
			if ((n / i) != i) {
				// if factor is even
				if ((n / i) % 2 == 0)
					even += (n / i);

				// if factor is odd
				else
					odd += (n / i);
			}
		}
	}
	// if n is odd
	if (n % 2 == 1)
		return 8 * (odd + even);

	// if n is even
	else
		return 24 * (odd);
}
// Driver code
int main()
{
    cout << "No. of ways of writing for n: " << endl;
	int n;
    cin >> n;

	cout << sum_of_4_squares(n) << endl;

	return 0;
}
