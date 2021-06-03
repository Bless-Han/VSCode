#include <iostream>
using std::cout;
#include "stonewt.h"
void display(const Stonewt & st, int n);
int main()
{
    Stonewt incognito = 275;
    Stonewt wolfe(285.7);
    Stonewt taft(21, 8);

    cout << "The celebrity weighed ";
    cout << incognito;
    cout << "The detective weighed ";
    cout << wolfe;
    cout << "The President weighed ";
    cout << taft;
    incognito = 276.8;
    taft = 325;
    cout << "After dinner, the celebrity weighed ";
    // incognito.show_stn();
    cout << incognito;
    cout << "After dinner, the President weighed ";
    // taft.show_lbs();
    taft.set_lbs();
    cout << taft;
    display(taft, 2);
    cout << "The wrestler weighed even more.\n";
    display(422, 2);
    cout << "No stone left unearned\n";
    return 0;
}

void display(const Stonewt & st, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << "Wow! ";
        cout << st;
    }
}