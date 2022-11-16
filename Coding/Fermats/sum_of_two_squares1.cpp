// A brute force approach based implementation
// to find if a number can be written as sum
// of two squares.
#include <bits/stdc++.h>
using namespace std;

// function to check if there exist two
// numbers sum of whose squares is n.
bool sumSquare(int n)
{
	for (long i = 1; i * i <= n; i++)
		for (long j = 1; j * j <= n; j++)
			if (i * i + j * j == n) {
				cout << i << "^2 + "
					<< j << "^2" << endl;
				return true;
			}
	return false;
}

// driver Program
int main()
{
	int n = 0;
    cin >> n;
	if (sumSquare(n))
		cout << "Yes\n";
	else
		cout << "No\n";
}
