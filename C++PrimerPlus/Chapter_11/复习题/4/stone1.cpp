#include <iostream>
#include "stonewt1.h"
int main()
{
    using std::cout;
    Stonewt temp(10, 8.0);
    Stonewt result = 2.0 * temp;
    // Stonewt result = temp * 2.0;
    result.show_stn();
    std::cout << "It's Ok!!\n";
    return 0;
}