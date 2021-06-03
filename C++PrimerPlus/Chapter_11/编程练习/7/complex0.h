#ifndef COMPLEX_H_
#define COMPLEX_H_
#include <iostream>
class complex
{
    private:
        double real;
        double imaginary;
    public:
        complex(double r, double i) { real = r; imaginary = i;}
        complex() { real = imaginary = 0.0; }
        complex operator~() const
            { return complex(real, -imaginary); }
        complex operator+(const complex & co) const 
            { return complex(real + co.real, imaginary + co.imaginary); }
        complex operator-(const complex & co) const
            { return complex(real - co.real, imaginary - co.imaginary); }
        complex operator*(const complex & co) const
            { return complex(real*co.real - imaginary*co.imaginary, real*co.imaginary + imaginary*co.real); }
        friend complex operator*(double n, const complex & co)
            { return complex(n * co.real, n * co.imaginary); }
        friend std::istream & operator>>(std::istream & is, complex & co);
        friend std::ostream & operator<<(std::ostream & os, const complex & co)
            {
                os << "(" << co.real << "," << co.imaginary << "i)";
                return os;
            }
};
#endif