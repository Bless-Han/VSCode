#include <iostream>
#include <cstring>
#include "golf.h"
using namespace std;
void setgolf(golf & g, const char * name, int hc)
{
    strcpy(g.fullname, name);
    g.handicap = hc;
}
int setgolf(golf & g)
{
    cout << "Enter the name: ";
    cin.getline(g.fullname, Len);
    if (!g.fullname[0])
        return 0;
    cout << "Enter the handicap: ";
    cin >> g.handicap;
    cin.get();
    return 1;
}
void handicap(golf & g, int hc)
{
    g.handicap = hc;
}
void showgolf(const golf & g)
{
    cout << "Name = " << g.fullname << endl;
    cout << "handicap = " << g.handicap << endl;
}