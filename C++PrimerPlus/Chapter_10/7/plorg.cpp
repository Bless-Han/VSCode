#include <iostream>
#include <cstring>
#include "plorg.h"
// static const int N = 20;
// char name[N];
// int ci;
void Plorg::show() const
{
    std::cout << "name = " << name << std::endl;
    std::cout << "ci = " << ci << std::endl;
}