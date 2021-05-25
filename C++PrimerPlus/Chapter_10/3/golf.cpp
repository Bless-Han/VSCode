#include <iostream>
#include <cstring>
#include "golf.h"
using namespace std;

Golf::Golf(const char * name, int hc)
{
    strcpy(this->fullname, name);
    this->handicap = hc;
}

Golf::Golf()
{
    setGolf();
}

void Golf::setGolf()
{
    cout << "Enter the name: ";
    cin.getline(this->fullname, this->LEN);
    if (!this->fullname[0])
        return;
    cout << "Enter the handicap: ";
    cin >> this->handicap;
    cin.get();
    return;
}

void Golf::setHandicap(int hc)
{
    handicap = hc;
}

void Golf::showGolf() const
{
    cout << "Name = " << fullname << endl;
    cout << "handicap = " << handicap << endl;
}