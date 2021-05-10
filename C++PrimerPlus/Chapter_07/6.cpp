#include <iostream>
using namespace std;
const int N = 10;
int Fill_array(double *a, int n);
void Show_array(double *a, int n);
void Reverse_array(double *a, int n);
int main()
{
    double a[N];
    int n = Fill_array(a, N);
    Show_array(a, n);
    Reverse_array(a, n);
    Show_array(a, n);
    Reverse_array(a + 1, n - 2);
    Show_array(a, n);
    return 0;
}
int Fill_array(double *a, int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        cin >> a[i];
        if (!cin)
            break;
    }
    return i;
}
void Show_array(double *a, int n)
{
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << endl;
}
void Reverse_array(double *a, int n)
{
    int temp{};
    for (int i = 0; i < n / 2; i++)
    {
        temp = a[i];
        a[i] = a[n-i-1];
        a[n-i-1] = temp;
    }
}