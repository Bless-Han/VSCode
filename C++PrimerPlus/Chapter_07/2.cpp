#include <iostream>
const int N = 10;
using namespace std;
int init(double * x, int n);
void show(double * x, int n);
double average(double * x, int n);
int main()
{
    double x[N];
    int n = init(x, N);
    show(x, n);
    cout << average(x, n) << endl;
    return 0;
}
int init(double * x, int n)
{
    int i{};
    for (i = 0; i < n; i++)
    {
        cin >> x[i];
        if (!cin)
            break;
    }
    return i;
}
void show(double * x, int n)
{
    for (int i = 0; i < n; i++)
        cout << x[i] << endl;
}
double average(double * x, int n)
{
    double sum{};
    for (int i = 0; i < n; i++)
        sum += x[i];
    return sum / n;
}