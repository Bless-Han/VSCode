#include <iostream>
#include "list.h"
void f(Item & i);
void f2(Item & i);
int main()
{
    List lst;
    lst.add(9);
    lst.add(11);
    lst.add(1);
    lst.add(19);
    lst.visit(f);
    lst.visit(f2);
    return 0;
}
void f(Item & i)
{
    i *= 2;
    std::cout << i << std::endl;
}
void f2(Item & i)
{
    i += 5;
    std::cout << i << std::endl;
}