#include <iostream>
#include <cctype>
using namespace std;
void f(string & s);
int main()
{
    string s;
    while(1)
    {
        cout << "Enter a string (q to quit): ";
        getline(cin, s);
        if (s.size() == 1 && s[0] == 'q')
            break;
        else
        {
            f(s);
            cout << s << endl;
        }
    }
    cout << "Bye\n";
    return 0;
}
void f(string & s)
{
    int len = s.size();
    for (int i = 0; i < len; i++)
        if (islower(s[i]))
            s[i] = toupper(s[i]);
}