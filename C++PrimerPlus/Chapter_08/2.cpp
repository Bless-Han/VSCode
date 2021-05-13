#include <iostream>
using namespace std;
struct CandyBar
{
    string name;
    double weight;
    int hots;
};
void set(CandyBar & c, const string name = "Millennium Munch",
    const double weight = 2.85, const int hots = 350);
void show(const CandyBar & c);
int main()
{
    struct CandyBar can;
    show(can);
    set(can);
    show(can);
    set(can, "Smith", 9.9, 99999);
    show(can);
    return 0;
}
void set(CandyBar & c, const string name,
    const double weight, const int hots)
{
    c.name = name;
    c.weight = weight;
    c.hots = hots;
}
void show(const CandyBar & c)
{
    cout << "name = " << c.name << endl;
    cout << "weight = " << c.weight << endl;
    cout << "hots = " << c.hots << endl;
}