#include <iostream>
using namespace std;
int main(){
  string fName;
  string lName;
  string allName;
  cout << "Enter your first name: ";
  getline(cin, fName);
  cout << "Enter your last name: ";
  getline(cin, lName);
  allName = lName + ", " + fName;
  cout << "Here's the information in a single string: " 
    << allName << endl;;
  return 0;
}
