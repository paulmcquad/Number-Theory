#include <vector>
#include <iostream>
using namespace std;

// Fermat polygonal number theorem

using V = std::vector < int > ;
V f(int n, int s) {
    V _ {0};

    int z = 1, a = 0, b = 1, i, t;
    for (; a < n; b += s - 2) _.push_back(a += b), ++z;
        V o;
    for (t = a = 0; t - n; b = ++a)
        for (o = V(s), t = i = 0; b; b /= z) t += o[i++] = _[b % z];
    return o;
}


void print(V x){
cout<<" [ ";
for (int e : x ){
 if(e!=0)
    cout << e << " ";
}
cout << "]\n";
}
void gonal (int n,int s){
cout << n<<", "<<s<<" => ";
print ( f(n,s));
}

int main() {

gonal(1,3);
gonal(2,3);
gonal(5,6);
gonal(17,3);
gonal(17,4);
gonal(17,5);
gonal(36,3);
gonal(43,6);
gonal(53,10);
gonal(879,17);
gonal(4856,23);
gonal(4,44);
gonal(5,100);

print ( f(53,3));
print ( f(1,4));
print ( f(3,4));
print ( f(4,4));
print ( f(44,4));
print ( f(100,5));
    return 0;
}