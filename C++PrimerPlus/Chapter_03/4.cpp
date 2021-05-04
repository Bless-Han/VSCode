#include <iostream>
using namespace std;

int main(){
  const int Hours_per_day = 24;
  const int Minutes_per_hour = 60;
  const int Seconds_per_minute = 60;
  cout << "Enter the nubmer of seconds: ";
  long long seconds{};
  cin >> seconds;
  int d = seconds / Seconds_per_minute / Minutes_per_hour / Hours_per_day;
  int h = seconds / Seconds_per_minute / Minutes_per_hour % Hours_per_day;
  int m = seconds / Seconds_per_minute - d * Hours_per_day * Minutes_per_hour - h * Minutes_per_hour;
  int s = seconds - m * Seconds_per_minute - h * Minutes_per_hour * Seconds_per_minute - d * Hours_per_day * Minutes_per_hour * Seconds_per_minute;
  cout << seconds << " seconds = " << d << " days, "
    << h << " hours, " << m << " minutes, "
    << s << " seconds" << endl;
  return 0;
}
