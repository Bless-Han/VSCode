#include <iostream>
#include <cctype>
#include "stack.h"
int main()
{
    Stack s;
    Item i1{"Smith", 900};
    Item i2{"Bless", 80};
    s.push(i1);
    s.push(i2);
    s.pop(i1);
    s.pop(i2);
    s.pop(i2);
    return 0;
}