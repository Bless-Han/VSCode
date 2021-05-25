#include <iostream>
#include "bank.h"
int main()
{
    Bank b{"Bless", 220111, 9999999};
    b.show();
    b.put(1);
    b.show();
    b.get(9000000000);
    b.show();
    return 0;
}