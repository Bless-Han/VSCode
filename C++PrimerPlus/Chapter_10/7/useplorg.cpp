#include "plorg.h"
int main()
{
    Plorg p1 = Plorg();
    Plorg p2 = Plorg("Bless", 20);
    p1.show();
    p2.show();
    p2.reset(30);
    p2.show();
    return 0;
}