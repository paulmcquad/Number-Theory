// Simple C++ program to find sum of series
// with cubes of first n natural numbers

// A000537 		Sum of first n cubes; or n-th triangular number squared. 
#include <iostream>
using namespace std;

/* Returns the sum of series */
int sumOfSeries(int n)
{
	int sum = 0;
	for (int x = 1; x <= n; x++)
		sum += x * x * x;
	return sum;
}

// Driver Function
int main()
{
	//int n = 5;
	int n =0;
	cin >> n;
	cout << sumOfSeries(n) << endl;
	return 0;
}
