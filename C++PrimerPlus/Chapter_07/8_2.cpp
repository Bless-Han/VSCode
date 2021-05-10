#include <iostream>
// #include <array>
#include <string>
using namespace std;
const int Seasons = 4;
const char * Snames[Seasons] = 
    {"Spring", "Summer", "Fall", "Winter"};
struct array
{
    double expenses[Seasons];
};
void fill(array *e);
void show(array e);

int main()
{
    array e;
    fill(&e);
    show(e);
    return 0;
}
void fill(array *e)
{
    for (int i = 0; i < Seasons; i++)
    {
        cout << "Enter " << Snames[i] << " expenses: ";
        cin >> e->expenses[i];
    }
}
void show(array e)
{
    double total = 0.0;
    cout << "\nEXPENSES\n";
    for (int i = 0; i < Seasons; i++)
    {
        cout << Snames[i] << ": $" << e.expenses[i] << endl;
        total += e.expenses[i];
    }
    cout << "Total Expenses: $" << total << endl;
}