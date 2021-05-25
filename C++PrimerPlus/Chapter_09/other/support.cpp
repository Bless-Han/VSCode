// 程序清单 9.6
#include <iostream>
extern double warming;

void update(double dtj);
void local();

using std::cout;
void update(double dt)
{
    extern double warming;
    warming += dt;
    cout << "Updating global warming to " << warming;
    cout << " degres.\n";
}

void local()
{
    double warming = 0.8;
    cout << "Local warming = " << warming << " degrees.\n";
    cout << "But global warming = " << ::warming;
    cout << " degrees.\n";
}
