#include <iostream>
#include "complex0.h"

// private:
double real;
double imaginary;
// public:
std::istream & operator>>(std::istream & is, complex & co)
{
    std::cout << "real: ";
    if (!(is >> co.real))
        return is;
    std::cout << "imaginary: ";
    is >> co.imaginary;
    return is;
}