#include <iostream>
#include <cstdlib>
#include <ctime>
#include "vect.h"
int main()
{
    using namespace std;
    using VECTOR::Vector;
    srand(time(0));
    double direction;
    Vector step;
    Vector result(0.0, 0.0);
    unsigned long steps = 0;
    double target;
    double dstep;
    int times;
    int min, max, average;
    int sum;
    cout << "Enter target distance (q to quit): ";
    while (cin >> target)
    {
        cout << "Enter step length: ";
        if (!(cin >> dstep))
            break;
        cout << "Enter times: ";
        if (!(cin >> times))
            break;
        min = 999999;
        sum = max = average = 0;
        for (int i = 0; i < times; i++)
        {
            while (result.magval() < target)
            {
                direction = rand() % 360;
                step.reset(dstep, direction, Vector::POL);
                result = result + step;
                steps++;
            }
            sum += steps;
            min = steps < min ? steps : min;
            max = steps > max ? steps : max;
            steps = 0;
            result.reset(0.0, 0.0);
        }
        cout << "min = " << min << endl;
        cout << "max = " << max << endl;
        cout << "average = " << 1.0 * sum / times << endl;
        // cout << "After " << steps << " steps, the subject "
        //         "has the following location:\n";
        // cout << result << endl;
        // result.polar_mode();
        // cout << "or \n" << result << endl;
        // cout << "Average outward distance per step = "
        //     << result.magval()/steps << endl;
        // steps = 0;
        // result.reset(0.0, 0.0);
        cout << "Enter target distance (q to quit): ";
    }
    cout << "Bye!\n";
    cin.clear();
    while (cin.get() != '\n')
        continue;
    return 0;
}