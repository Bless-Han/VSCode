#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int count{};
    char ch;
    ifstream inFile;
    inFile.open("8.txt");
    while (inFile.get(ch))
    {
        count++;
    }

    cout << "count = " << count << endl;
    return 0;
}