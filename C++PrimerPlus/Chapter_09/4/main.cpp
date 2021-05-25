#include <iostream>
#include "sales.h"
using namespace std;
using namespace SALES;
void f()
{
    cout << "This is a test.\n";
}
int main()
{
    double a[4] = {2.2, 3.3, 4.4, 5.9};
    Sales s1;
    Sales s2;
    setSales(s1, a, 4);
    setSales(s2);
    showSales(s1);
    showSales(s2);
    return 0;
}