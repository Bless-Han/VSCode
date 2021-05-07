#include <iostream>
#include <fstream>
const int N = 20;
using namespace std;
struct patrons {
    string name;
    double money;
};
int main()
{
    ifstream inFile;
    inFile.open("9.txt");
    auto pa = new patrons[N];
    int i{};
    for ( ; getline(inFile, pa[i].name); ++i){
        inFile >> pa[i].money;
        inFile.get();
    }
    cout << "Grand Patrons\n";
    for (int j = 0; j < i; ++j)
    {
        if (pa[j].money >= 10000)
            cout << pa[j].name << endl;
    }
    cout << "\nPatrons\n";
    for (int j = 0; j < i; ++j)
    {
        if (pa[j].money < 10000)
            cout << pa[j].name << endl;
    }
    delete [] pa;
    return 0;
}