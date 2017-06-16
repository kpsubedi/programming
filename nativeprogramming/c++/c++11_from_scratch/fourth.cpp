#include <iostream>

using namespace std;

int main(){
    double fahrenheit{};
    double celsius{};

    cout << "Please enter a temperature value in Fahrenheit: ";
    cin >> fahrenheit;
    
    celsius = (fahrenheit - 32.0)*5.0/9.0;

    cout << "The corresponding value in Celsius is: " << celsius << '\n';
}

