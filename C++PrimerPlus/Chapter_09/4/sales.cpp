#include <iostream>
#include "sales.h"
using namespace SALES;
using namespace std;
namespace SALES
{
    void setSales(Sales & s, const double ar[], int n)
    {
        double sum{};
        double max{};
        double min{};
        for (int i = 0; i < n; i++)
        {
            s.sales[i] = ar[i];
            sum += s.sales[i];
            if (i == 0)
            {
                min = max = s.sales[i];
            }
            else
            {
                if (s.sales[i] < min)
                    min = s.sales[i];
                if (s.sales[i] > max)
                    max = s.sales[i];
            }
        }
        s.average = sum / n;
        s.min = min;
        s.max = max;
    }
    void setSales(Sales & s)
    {
        double sum{};
        double max{};
        double min{};
        for (int i = 0; i < QUARTERS; i++)
        {
            cout << i + 1 << ": ";
            cin >> s.sales[i];
            sum += s.sales[i];
            if (i == 0)
            {
                min = max = s.sales[i];
            }
            else
            {
                if (s.sales[i] < min)
                    min = s.sales[i];
                if (s.sales[i] > max)
                    max = s.sales[i];
            }
        }
        s.average = sum / QUARTERS;
        s.min = min;
        s.max = max;
    }
    void showSales(const Sales & s)
    {
        for (int i = 0; i < QUARTERS; i++)
            cout << i + 1 << " = " << s.sales[i] << endl;
        cout << "average = " << s.average << endl;
        cout << "max = " << s.max << endl;
        cout << "min = " << s.min << endl;
    }
}