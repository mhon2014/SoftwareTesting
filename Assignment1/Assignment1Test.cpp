#include <iostream>
#include <vector>
#include <bitset>

int main(){
    std::cout << "Hello\n";
    std::bitset<20000000> test;
    std::cout << "big riiiip Size" << sizeof(test) << "\n";
    return 0;
}