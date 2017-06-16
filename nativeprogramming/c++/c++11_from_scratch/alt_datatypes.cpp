#include <iostream>
#include <limits>
using namespace std;

int main(){
    cout << " int type\n";
    cout << " --------\n";
    cout << " Size: " << sizeof(int) << " bytes\n";
    cout << " Max: " << numeric_limits<int>::max() << '\n';
    cout << " Min: " << numeric_limits<int>::min() << '\n';
}

