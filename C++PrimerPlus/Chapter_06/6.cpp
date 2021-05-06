#include <iostream>
using namespace std;
struct patrons {
    string name;
    double money;
};
int main()
{
    int n;
    cin >> n;
    auto pa = new patrons[n];
    for (int i = 0; i < n; ++i)
        cin >> pa[i].name >> pa[i].money;
    cout << "Grand Patrons\n";
    for (int i = 0; i < n; ++i)
    {
        if (pa[i].money >= 10000)
            cout << pa[i].money << endl;
    }
    cout << "Patrons\n";
    for (int i = 0; i < n; ++i)
    {
        if (pa[i].money < 10000)
            cout << pa[i].money << endl;
    }
    delete [] pa;
    return 0;
}