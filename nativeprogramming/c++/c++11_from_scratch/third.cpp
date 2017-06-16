#include <iostream>

using namespace std;

int main(){
    cout << " a = ? ";
    int a{};
    cin >> a;

    cout << " b = ? ";
    int b{};
    cin >> b;

    cout << '\n';
    cout << " a + b = " << (a + b) << "\n";
    cout << " a - b = " << (a - b) << '\n';
    cout << " a * b = " << (a * b) << "\n";
    cout << " a / b = " << (a / b) << "\n";
    cout << " a % b = " << (a % b) << "\n";
}
