#include <iostream>
#include <cstring>
using namespace std;
int main(){
  const int N(50);
  char fName[N];
  char lName[N];
  char allName[N];
  cout << "Enter your first name: ";
  cin >> fName;
  cout << "Enter your last name: ";
  cin >> lName;
  strcpy(allName, lName);
  strcat(allName, ", ");
  strcat(allName, fName);
  cout << "Here's the information in a single string: " 
    << allName << endl;
  return 0;
}
