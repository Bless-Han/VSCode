#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <math.h>
using namespace std;

struct node {
    set<int> he, buhe;
};

int main()
{
    vector<node> v(13);
    int temp, n, xx;
    for (int i = 1; i < 13; i++)
    {
        cin >> xx;
        cin >> n;
        for (int j = 0; j < n; j++)
        {
            cin >> temp;
            v[xx].he.insert(temp);
        }
        cin >> n;
        for (int j = 0; j < n; j++)
        {
            cin >> temp;
            v[xx].buhe.insert(temp);
        }
    }
    cin >> n;
    int a, b;
    for (int i = 0; i < n; i++)
    {
        cin >> a >> b;
        if (v[a].he.count(b) and v[b].he.count(a))
            cout << "Yes" << endl;
        else if (v[a].buhe.count(b) and v[b].buhe.count(a))
            cout << "No" << endl;
        else
            cout << "NA" << endl;
    }
}