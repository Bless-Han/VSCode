#include <iostream>
using namespace std;
const int Max = 5;

double *fill_array(double *begin, double *end);
void show_array(const double *begin, double *end);
void revalue(double r, double *begin, double *end);
int main()
{
    double properties[Max];
    double *end = fill_array(properties, properties + Max);
    show_array(properties, end);
    if (end - properties > 0)
    {
        cout << "Enter revaluation factor: ";
        double factor;
        while (!(cin >> factor))
        {
            cin.clear();
            while (cin.get() != '\n')
                continue;
            cout << "Bad input; Please enter a number: ";
        }
        revalue(factor, properties, end);
        show_array(properties, end);
    }
    cout << "Done.\n";
    return 0;
}
double *fill_array(double *begin, double *end)
{
    double temp;
    double * pd;
    for (pd = begin; pd != end; pd++)
    {
        cout << "Enter value #" << (pd - begin + 1) << ": ";
        cin >> temp;
        if (!cin)
        {
            cin.clear();
            while (cin.get() != '\n')
                continue;
            cout << "Bad input; input process terminated.\n";
            break;
        }
        else if (temp < 0)
            break;
        *pd = temp;
    }
    return pd;
}
void show_array(const double *begin, double *end)
{
    for (const double *pd = begin; pd != end; pd++)
    {
        cout << "Property #" << (pd - begin + 1) << ": $";
        cout << *pd << endl;
    }
}
void revalue(double r, double *begin, double *end)
{
    for (double *pd = begin; pd != end; pd++)
        *pd *= r;
}