// CPP program to verify Nicomachu's Theorem
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int NicomachuTheorem_sum(int n)
{
// Compute sum of cubes
int sum = 0;
for (int k=1; k<=n; k++)
	sum += k*k*k;
	
// Check if sum is equal to
// given formula.
int triNo = n*(n+1)/2;
if (sum == triNo * triNo)
	cout << "Yes\n";
else
	cout << "No\n";

    return sum;
}

// driver function
int main()
{

    // int n = 5;
	int n = 0;
	cin >> n;
	cout << NicomachuTheorem_sum(n) << endl;
    
	return 0;
}
