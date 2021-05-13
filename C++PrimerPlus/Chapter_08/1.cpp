#include <iostream>
using namespace std;
void show(const char * str, int n = 1);
int main()
{
    show("This is a test.");
    show("This is a test.", 9);
    show("This is a test.", 6);
    return 0;
}
void show(const char * str, int n)
{
    if (n)
        cout << str << endl;
}