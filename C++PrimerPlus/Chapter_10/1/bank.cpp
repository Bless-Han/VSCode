#include <iostream>
#include "bank.h"

// std::string name;
// int number;
// double money;
Bank::Bank(std::string str, int num, double m)
{
    name = str;
    number = num;
    money = m;
}
Bank::~Bank()
{
    std::cout << "Bye " << name << std::endl;
}
void Bank::show() const
{
    using std::ios_base;
    using std::cout;
    using std::endl;
    ios_base::fmtflags orig = cout.setf(ios_base::fixed);
    std::streamsize prec = cout.precision(3);

    cout << "name = " << name << endl;
    cout << "number = " << number << endl;
    cout << "money = " << money << endl;
    cout.setf(orig, ios_base::floatfield);
    cout.precision(prec);
}
void Bank::put(double m)
{
    money += m;
}
void Bank::get(double m)
{
    if (money < m)
        std::cout << "Not enough money\n";
    else
        money -= m;
}