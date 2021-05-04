#include <iostream>
using namespace std;
void show();
void showError();
void showCarnivore();
void showPianist();
void showTree();
void showGame();
int judge(char ch);
int main()
{
  show();
  char ch;
  while ((ch = cin.get()) && !judge(ch))
    showError();
  switch (ch)
  {
    case 'c' : showCarnivore(); break;
    case 'p' : showPianist(); break;
    case 't' : showTree(); break;
    case 'g' : showGame(); break;
    default : showError(); break;
  }
  return 0;
}
void show()
{
  cout << "Please enter one of the following choices: \n";
  cout << "c) carnivore           p) pianist\n";
  cout << "t) tree                g) game\n";
}
void showError()
{
  cout << "Please enter a c, p, t, or g: ";
}
void showCarnivore()
{
  cout << "A maple is a carnivore.\n";
}
void showPianist()
{
  cout << "A maple is a pianist.\n";
}
void showTree()
{
  cout << "A maple is a tree.\n";
}
void showGame()
{
  cout << "A maple is a game.\n";
}
int judge(char ch)
{
  if (ch == 'c' || ch == 'p' || ch == 't' || ch == 'g')
    return true;
  else  
    return false;
}
