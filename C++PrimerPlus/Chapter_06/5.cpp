#include <iostream>
using namespace std;
struct shuishou {
    double tvarps;
    double count(){
        double ret{};
        if (tvarps > 35000)
            ret = 10000 * 0.1 + 20000 * 0.15 + (tvarps - 35000) * 0.2;
        else if (tvarps > 15000)
            ret = 10000 * 0.1 + (tvarps - 25000) * 0.15;
        else if (tvarps > 5000)
            ret = (tvarps - 5000) * 0.1;
        return ret;
    }
};
int main()
{
    shuishou * ss = new shuishou;
    double temp{};
    while (cin >> temp && temp)
    {
        ss->tvarps = temp;
        cout << ss->count() << endl;
    }
    delete ss;
    return 0;
}