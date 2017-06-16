#include <iostream>
#include <limits>

int main(){
    std::cout << " int type\n";
    std::cout << " --------\n";
    std::cout << " Size: " << sizeof(int) << " bytes\n";
    std::cout << " Max: " << std::numeric_limits<int>::max() << '\n';
    std::cout << " Min: " << std::numeric_limits<int>::min() << '\n';
}

