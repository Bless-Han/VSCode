#include <iostream>
#include <cstring>
using namespace std;
const int N = 20;
int main()
{
  cout << "Enter words (to stop, type the word done):" << endl;
  char words[N];
  int count = 0;
  cin >> words;
  while (strcmp(words, "done")) 
  {
    ++count;
    cin >> words;
  }
  cout << "You entered a total of " << count 
    << " words." << endl;
  return 0;
}
