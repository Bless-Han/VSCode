#include <iostream>
#include <cstdlib>
#include <ctime>
#include "vect.h"
int main()
{
    using namespace std;
    using VECTOR::Vector;
    Vector v(50.0, 200.0, Vector::POL);
    cout << v << endl;
    double a = v;
    cout << a << endl;
    return 0;
}