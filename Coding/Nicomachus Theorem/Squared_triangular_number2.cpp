// A formula based C++ program to find sum
// of series with cubes of first n natural
// numbers

// A000537 		Sum of first n cubes; or n-th triangular number squared. 
#include <iostream>
using namespace std;

int sumOfSeries(int n)
{
	int x = (n * (n + 1) / 2);
	return x * x;
}

// Driver Function
int main()
{
	int n =0;
	cin >> n;
	cout << sumOfSeries(n) << endl;
	return 0;
}
