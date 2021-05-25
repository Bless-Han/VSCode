#include <iostream>
#include "sales.h"
using namespace SALES;
using namespace std;
Sales::Sales(const double ar[], int n)
{
    double sum{};
    double max{};
    double min{};
    for (int i = 0; i < n; i++)
    {
        this->sales[i] = ar[i];
        sum += this->sales[i];
        if (i == 0)
        {
            min = max = this->sales[i];
        }
        else
        {
            if (this->sales[i] < min)
                min = this->sales[i];
            if (this->sales[i] > max)
                max = this->sales[i];
        }
    }
    this->average = sum / n;
    this->min = min;
    this->max = max;
}
Sales::Sales()
{
    double sum{};
    double max{};
    double min{};
    for (int i = 0; i < QUARTERS; i++)
    {
        cout << i + 1 << ": ";
        cin >> this->sales[i];
        sum += this->sales[i];
        if (i == 0)
        {
            min = max = this->sales[i];
        }
        else
        {
            if (this->sales[i] < min)
                min = this->sales[i];
            if (this->sales[i] > max)
                max = this->sales[i];
        }
    }
    this->average = sum / QUARTERS;
    this->min = min;
    this->max = max;

}
void Sales::showSales() const
{
    for (int i = 0; i < QUARTERS; i++)
        cout << i + 1 << " = " << this->sales[i] << endl;
    cout << "average = " << this->average << endl;
    cout << "max = " << this->max << endl;
    cout << "min = " << this->min << endl;
}