#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <math.h>
using namespace std;

bool isvalid(int x);
int sm(string s);
int main()
{
    int n, cnt = 0, m = 0;
    int num;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        if (isvalid(num))
        {
            cnt++;
            max(m, num);
        }
    }
    cout << cnt << endl;
    cout << m << endl;
}
bool isvalid(int x)
{
    if (x <= 0 or x % 2 == 1)
        return false;
    bool down = true;
    int mid = 0;
    string s = to_string(x);
    for (int i = 0; i < s.size() - 1; i++)
    {
        if (down == true)
        {
            if (s[i] - '0' <= s[i + 1] - '0') 
            {
                down = false;
                mid = i;
            }
        }
        else if (s[i] - '0' > s[i + 1] - '0')
            return false;
    }
    int left = sm(s.substr(0, mid+1));
    int right = sm(s.substr(mid, s.size()));
    if (left % 2 == right % 2)
        return false;
    return true;
}
int sm(string s)
{
    int res = 0;
    for (int i = 0; i < s.size(); i++)
    {
        res += s[i] - '0';
    }
    return res;
}