// CPP program for Lagrange's four square identity
#include <bits/stdc++.h>
using namespace std;

// Prints all the possible combinations 4 numbers
// whose sum of squares is equal to the given no.
void printFourSquares(int a)
{
	// loops checking the sum of squares
	for (int i = 0; i * i <= a; i++) {
		for (int j = i; j * j <= a; j++) {
			for (int k = j; k * k <= a; k++) {
				for (int l = k; l * l <= a; l++) {

					// if sum of four squares equals
					// the given no.
					if (i * i + j * j + k * k + l * l == a) {

						// printing the numbers
						cout << a << " = " << i << "*" << i
							<< " + " << j << "*" << j << " + ";
						cout << k << "*" << k << " + "
							<< l << "*" << l << "\n";
					}
				}
			}
		}
	}
}

// Driver Code
int main()
{
	int a = 74;
	// 74 = 0*0 + 0*0 + 5*5 + 7*7
	// 74 = 0*0 + 1*1 + 3*3 + 8*8
	// 74 = 0*0 + 3*3 + 4*4 + 7*7
	// 74 = 1*1 + 1*1 + 6*6 + 6*6
	// 74 = 2*2 + 3*3 + 5*5 + 6*6

	printFourSquares(a);

	return 0;
}
