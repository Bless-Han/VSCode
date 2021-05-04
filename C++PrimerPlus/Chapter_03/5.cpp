#include <iostream>
using namespace std;

int main(){
  cout << "Enter the world's population: ";
  long long world_population{};
  cin >> world_population;
  cout << "Enter the population of the US: ";
  long long US_Population{};
  cin >> US_Population;
  cout << "The population of the US is "
    << double(100.0 * US_Population / world_population)
    << "% of the world population." << endl;
  return 0;
}
