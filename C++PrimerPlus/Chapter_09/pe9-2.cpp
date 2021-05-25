#include <iostream>
using std::string;
// const int ArSize = 10;
void strcount(string str);
int main()
{
    using namespace std;
    // char input[ArSize];
    string input;
    char next;

    cout << "Enter a line:\n";
    getline(cin, input);
    // cin.get(input,ArSize);
    while(input != "")
    {
        // cin.get(next);
        // while (next != '\n')
        //     cin.get(next);
        strcount(input);
        cout << "Enter next line (empty line to quit):\n";
        getline(cin, input);
        // cin.get(input, ArSize);
    }
    cout << "Bye\n";
    return 0;
}
void strcount(string str)
{
    using namespace std;
    static int total = 0;
    int count = 0;

    cout << "\"" << str << "\" contains ";
    // while (*str++)
    //     count++;
    count = str.size();
    total += count;
    cout << count << " characters\n";
    cout << total << " characters total\n";
}