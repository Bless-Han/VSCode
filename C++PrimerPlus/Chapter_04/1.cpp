#include <iostream>
using namespace std;

int main(){
  string fName;
  string lName;
  char grade;
  int age;
  cout << "What is your first name? ";
  getline(cin, fName);
  cout << "What is your last name? ";
  getline(cin, lName);
  cout << "What letter grade do you deserve? ";
  cin >> grade;
  grade++;
  cout << "What is your age? ";
  cin >> age;
  cout << "Name: " << lName << ", "
    << fName << endl;
  cout << "Grade: " << grade << endl;
  cout << "Age: " << age << endl;
  return 0;
}
