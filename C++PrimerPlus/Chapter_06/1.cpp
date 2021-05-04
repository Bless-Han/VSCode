#include <iostream>
#include <cctype>
using namespace std;
int main()
{
  char ch;
  while ((ch = cin.get()) != '@')
  {
    {
      if (islower(ch))
        cout << char(toupper(ch));
      else if (isupper(ch))
        cout << char(tolower(ch));
      else if (!isdigit(ch))
        cout << ch;
    }
  }
  return 0;
}
