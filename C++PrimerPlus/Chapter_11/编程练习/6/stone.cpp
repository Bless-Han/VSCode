#include <iostream>
using std::cout;
#include "stonewt.h"
int main()
{
    Stonewt temp(11, 0.0);
    int i;
    Stonewt sts[6] = 
    {
        Stonewt(10, 5.0),
        Stonewt(20, 3.9),
        Stonewt(9, 2.0)
    };
    int tmp_stone;
    double tmp_pounds;
    for (i = 3; i < 6; i++)
    {
        cout << i + 1 << ":\nEnter the stone: ";
        std::cin >> tmp_stone;
        cout << "Enter the pounds: ";
        std::cin >> tmp_pounds;
        sts[i] = Stonewt(tmp_stone, tmp_pounds);
    }
    Stonewt max, min(9999, 1.0);
    cout << ">= 11 Stone:\n";
    for (i = 0; i < 6; i++)
    {
        if (sts[i] >= temp)
            cout << sts[i];
        max = sts[i] > max ? sts[i] : max;
        min = sts[i] < min ? sts[i] : min;
    }
    cout << "min = " << min << std::endl;
    cout << "max = " << max << std::endl;
}