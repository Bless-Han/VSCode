#include <iostream>
using namespace std;
const int N = 20;
const int K = 5;
struct bop {
  char fullname[N];
  char title[N];
  char bopname[N];
  int preference;
};
void show();
void showChoice();
void showError();
bool judge(char ch);
void showBye();
void showA(bop * b);
void showB(bop * b);
void showC(bop * b);
void showD(bop * b);
void begin(bop * b);
int main()
{
  auto b = new bop[K];
  b[0].preference = 0;
  b[1].preference = 1;
  b[2].preference = 2;
  b[3].preference = 1;
  b[4].preference = 1;
  begin(b);
  show();
  showChoice();
  char ch{};
  // while ((ch = cin.get()) != EOF)
  while (1)
  {
    cin >> ch;
    if (!judge(ch))
    {
      showError();
      continue;
    }
    switch (ch) {
      case 'a' : showA(b); break;
      case 'b' : showB(b); break;
      case 'c' : showC(b); break;
      case 'd' : showD(b); break;
    }
    if (ch == 'q')
    {
      showBye();
      break;
    }
  }
  delete [] b;
  return 0;                                                   
}
void show()
{
  cout << "Benevolent Order of Programmers Report\n";
  cout << "a. displa by name        b. display by title\n";
  cout << "c. display by bopname    d. display by preference\n";
  cout << "q. quit\n";
}
void showError()
{
  cout << "Please enter a a, b, c, d, or q: \n";
}
bool judge(char ch)
{
  if (ch == 'a' || ch == 'b' || ch == 'c' || ch == 'd' || ch == 'q')
    return true;
  else 
    return false;
}
void showChoice()
{
  cout << "Enter your choice: \n";
}
void showBye()
{
  cout << "Bye!\n";
}
void showA(bop * b)
{
  for (int i = 0; i < K; i++)
    cout << b[i].fullname << endl;
}
void showB(bop * b)
{
  for (int i = 0; i < K; i++)
    cout << b[i].title << endl;
}
void showC(bop * b)
{
  for (int i = 0; i < K; i++)
    cout << b[i].bopname << endl;
}
void showD(bop * b)
{
  for (int i = 0; i < K; i++)
  {
    switch (b[i].preference)
    {
      case 0 : 
        cout << b[i].fullname << endl;
        break;
      case 1 : 
        cout << b[i].title << endl;
        break;
      case 2 : 
        cout << b[i].bopname << endl;
        break;
    }
  }
}
void begin(bop * b)
{
  int n;
  for (int i = 0; i < K; i++)
  {
    cin.getline(b[i].fullname, N);
    cin.getline(b[i].title, N);
    cin.getline(b[i].bopname, N);
    cin.get();
    cin >> n;
    // cin >> b[i].preference;
    cin.clear();
    // cout << "#" << i+1 << " is began." << endl;
    // cout << b[i].fullname << endl
      // << b[i].title << endl
      // << b[i].bopname << endl
      // << b[i].preference << endl;
  }
}
