#include <iostream>
using namespace std;
#include <cstring>
struct stringy
{
    char * str;
    int ct;
};
void set(stringy & str, const char * c);
void show(const stringy str, int n = 1);
void show(const char *str, int n = 1);

int main()
{
    struct stringy beany;
    char testing[] = "Reality isn't what it used to be.";

    set(beany, testing);
    show(beany);
    testing[0] = 'D';
    testing[1] = 'u';
    show(testing);
    show(testing, 3);
    show("Donw!");
    delete(beany.str);
    return 0;
}
void set(stringy & str, const char * c)
{
    int len = strlen(c);
    str.ct = len;
    str.str = new char[len];
    strcpy(str.str, c);
}
void show(const stringy str, int n)
{
    for (int i = 0; i < n; i++)
        cout << str.str << endl;
}
void show(const char *str, int n)
{
    for (int i = 0; i < n; i++)
        cout << str << endl;
}