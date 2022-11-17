// Efficient CPP program to find sum of cubes
// of first n natural numbers that avoids
// overflow if result is going to be with in
// limits.

// A000537 		Sum of first n cubes; or n-th triangular number squared. 
#include <iostream>
using namespace std;

// Returns sum of first n natural
// numbers
int sumOfSeries(int n)
{
	int x;
	if (n % 2 == 0)
		x = (n / 2) * (n + 1);
	else
		x = ((n + 1) / 2) * n;
	return x * x;
}

// Driver code
int main()
{
	int n =0;
	cin >> n;
	cout << sumOfSeries(n) << endl;
	return 0;
}
