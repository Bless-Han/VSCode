#include <iostream>
using namespace std;
inline double calculate(double a, double b, double (*f[])(double a, double b));
double f1(double a, double b);
double f2(double a, double b);
int main()
{
    double a, b;
    double (*f[2])(double a, double b) = {f1, f2};
    while (1)
    {
        cin >> a >> b;
        if (!cin)
            break;
        cout << "result = " << calculate(a, b, f) << endl;
    }
    return 0;
}
inline double calculate(double a, double b, double (*f[])(double a, double b))
{
    return f[0](a, b) + f[1](a, b);
}
double f1(double a, double b)
{
    return a * b;
}
double f2(double a, double b)
{
    return a + b;
}