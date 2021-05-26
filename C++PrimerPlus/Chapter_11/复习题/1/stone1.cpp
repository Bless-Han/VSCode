#include <iostream>
#include "stonewt1.h"
int main()
{
    using std::cout;
    Stonewt temp(10, 8.0);
    Stonewt result = temp * 2.0;
    result.show_stn();
    return 0;
}