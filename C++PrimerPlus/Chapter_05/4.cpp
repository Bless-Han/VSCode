#include <iostream>
using namespace std;
const double Daphne = 10.0 / 100;
const double Cleo = 5.0 / 100;
int main(){
  double daphne, cleo;
  daphne = cleo = 100;
  int count = 0;
  do {
    cleo += cleo * Cleo;
    daphne += 100 * Daphne;
    count++;
    cout << count << " years: " 
      << "cleo = " << cleo
      << ", daphne = " << daphne 
      << endl;
  } while (cleo <= daphne);
  return 0;
}
