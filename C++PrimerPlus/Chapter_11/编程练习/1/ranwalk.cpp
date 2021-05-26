#include <iostream>
#include <fstream>
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
    ofstream os;
    os.open("outPut");
    unsigned long steps = 0;
    double target;
    double dstep;
    cout << "Enter target distance (q to quit): ";
    int i;
    while (cin >> target)
    {
        cout << "Enter step length: ";
        if (!(cin >> dstep))
            break;
        os << "Target Distance: " << target << ", Step Size: " << dstep << endl;
        i = 0;
        while (result.magval() < target)
        {
            os << i++ << ": " << result << endl;
            direction = rand() % 360;
            step.reset(dstep, direction, Vector::POL);
            result = result + step;
            steps++;
        }
        os << "After " << steps << " steps, the subject "
                "has the following location:\n";
        os << result << endl;
        result.polar_mode();
        os << "or \n" << result << endl;
        os << "Average outward distance per step = "
            << result.magval()/steps << endl;
        steps = 0;
        result.reset(0.0, 0.0);
        cout << "Enter target distance (q to quit): ";
    }
    os << "Bye!\n";
    cin.clear();
    while (cin.get() != '\n')
        continue;
    return 0;
}