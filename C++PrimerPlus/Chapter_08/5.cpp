#include <iostream>
using namespace std;
template <class T>
T max5(T a[5]);
int main()
{
    int i[5] = {1, 3, 2, 200, 50};
    double d[5] = {2.5, 9.9, 3.4, 4.4, 5.5};
    cout << max5(i) << endl;
    cout << max5(d) << endl;
    return 0;
}
template <class T>
T max5(T a[5])
{
    T ret = a[0];
    for (int i = 1; i < 5; i++)
    {
        if (a[i] > ret)
            ret = a[i];
    }
    return ret;
}