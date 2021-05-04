#include <iostream>
int main(){
  using namespace std;
  cout << "Enter a latitude in degrees, minutes, and seconds:" << endl;
  int degrees, minutes, seconds;
  cout << "First, enter the degrees: ";
  cin >> degrees;
  cout << "Next, enter the minutes of arc: ";
  cin >> minutes;
  cout << "Finally, enter the seconds of arc: ";
  cin >> seconds;
  double result = degrees + minutes / 60.0 + seconds / 60.0 / 60.0;
  cout << degrees << " degrees, " << minutes << " minutes, "
    << seconds << " seconds = " << result << " degrees" << endl;
  return 0;
}
