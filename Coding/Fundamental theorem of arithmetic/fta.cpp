// Description: Print all the prime factors of a given number.
// Author     : Paul McQuade <paulmcquad@gmail.com>
// License    : GPLv3


#include <iostream>
#include <string>

using namespace std;

int main() {
	
	//declare variable
	int N, i, fm, Num;
	
    cout << "Type in No. to factor:" << endl;
	cin>> N;
	Num = N;
	
	i = 2;
	string result = "";
	
	do {
		fm = 0;
		while(N % i == 0) {
            fm++;
            N /= i;
	}
	
	if( fm ) {
		string result2 = to_string(i) + "^" + to_string(fm) + " * ";
		result = result.append(result2);
	}
	
	i++;
		
	} while(!(N == 1));
        result = result.substr(0, result.length() - 3);
	cout<<  Num <<" = "<<  result;
	
	return 0;
}