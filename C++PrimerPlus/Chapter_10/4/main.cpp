#include <iostream>
#include "sales.h"
using namespace std;
using namespace SALES;
int main()
{
    double a[4] = {2.2, 3.3, 4.4, 5.9};
    Sales s1(a, 3);
    Sales s2 = Sales();
    s1.showSales();
    s2.showSales();
    return 0;
}