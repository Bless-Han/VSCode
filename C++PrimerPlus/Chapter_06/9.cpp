#include <iostream>
#include <fstream>
const int N = 20;
const int S = 100;
using namespace std;
struct patrons {
    char name[S];
    double money;
};
int main()
{
    ifstream inFile;
    inFile.open("9.txt");
    auto pa = new patrons[N];
    int i{};
    for ( ; inFile.getline(pa[i].name, S); ++i){
        inFile >> pa[i].money;
    }
    cout << "Grand Patrons\n";
    for (int j = 0; j < i; ++j)
    {
        if (pa[j].money >= 10000)
            cout << pa[j].name << endl;
    }
    cout << "Patrons\n";
    for (int j = 0; j < i; ++j)
    {
        if (pa[j].money < 10000)
            cout << pa[j].name << endl;
    }
    delete [] pa;
    return 0;
}