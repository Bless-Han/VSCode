#include <iostream>
#include <cstring>
using namespace std;
template <typename T>
T maxn(T a[], int n);

template <> const char * maxn<const char *>(const char *s[], int n);
int main()
{
    int i[6] = {9, 1, 3, 2, 200, 50};
    double d[4] = {9.9, 3.4, 4.4, 5.5};
    cout << maxn(i, 6) << endl;
    cout << maxn(d, 4) << endl;
    const char *str[ ] = 
    {
        "This is a test.",
        "This is another test",
        "This is another another test.",
        "World"
    };
    const char *str2 = maxn(str, 3);
    cout << str2 << endl;
    return 0;
}
template <typename T>
T maxn(T a[], int n)
{
    T ret = a[0];
    for (int i = 1; i < n; i++)
    {
        if (a[i] > ret)
            ret = a[i];
    }
    return ret;
}
template <> const char * maxn<const char *>(const char *s[], int n)
{
    const char * ret = s[0];
    int len = strlen(s[0]);
    // cout << "len = " << len << endl;
    for (int i = 1; i < n; i++)
    {
        if (int(strlen(s[i])) > len)
        {
            ret = s[i];
            len = strlen(s[i]);
        }
    }
    return ret;
}