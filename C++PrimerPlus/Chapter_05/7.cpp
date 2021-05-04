#include <iostream>
using namespace std;

struct car 
{
  string madeIn;
  int year;
};
int main()
{
  cout << "How many cars do you wish to catalog? ";
  int n;
  cin >> n;
  cin.get();
  car * cars = new car[n];
  for (int i = 0; i < n; ++i)
  {
    cout << "Car #" << i + 1 << ":" << endl;
    cout << "Please enter the make: ";
    getline(cin, cars[i].madeIn);
    cout << "Please enter the year made: ";
    cin >> cars[i].year;
    cin.get();
  }
  for (int i = 0; i < n; ++i) 
    cout << cars[i].year << " " << cars[i].madeIn << endl;
  delete [] cars;
  return 0;
}
