#include <iostream>
using namespace std;
double f(double x, double y);
int main()
{
    int a, b;
    cin >> a >> b;
    while (a != 0 && b != 0)
    {
        cout << f(a, b) << endl;
        cin >> a >> b;
    }

    return 0;
}
double f(double x, double y)
{
    return 2.0 * x * y / (x + y);
}