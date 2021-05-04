#include <iostream>
using namespace std;
int main()
{
  cout << "Enter words (to stop, type the word done):" << endl;
  string words;
  int count = 0;
  cin >> words;
  while (words != "done") 
  {
    ++count;
    cin >> words;
  }
  cout << "You entered a total of " << count 
    << " words." << endl;
  return 0;
}
