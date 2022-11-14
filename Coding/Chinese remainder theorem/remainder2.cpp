// Requires C++17
#include <iostream>
#include <numeric>
#include <vector>
#include <execution>

using namespace std;

template<typename _Ty> _Ty mulInv(_Ty a, _Ty b) {
	_Ty b0 = b;
	_Ty x0 = 0;
	_Ty x1 = 1;

	if (b == 1) {
		return 1;
	}

	while (a > 1) {
		_Ty q = a / b;
		_Ty amb = a % b;
		a = b;
		b = amb;

		_Ty xqx = x1 - q * x0;
		x1 = x0;
		x0 = xqx;
	}

	if (x1 < 0) {
		x1 += b0;
	}

	return x1;
}

template<typename _Ty> _Ty chineseRemainder(std::vector<_Ty> n, std::vector<_Ty> a) {
	_Ty prod = std::reduce(std::execution::seq, n.begin(), n.end(), (_Ty)1, [](_Ty a, _Ty b) { return a * b; });

	_Ty sm = 0;
	for (int i = 0; i < n.size(); i++) {
		_Ty p = prod / n[i];
		sm += a[i] * mulInv(p, n[i]) * p;
	}

	return sm % prod;
}

int main() {
	vector<int> num{3, 4, 5};
	vector<int> rem{2, 3, 1};

    
	cout << "x is "  << chineseRemainder(num,rem) << endl;

	return 0;
}
