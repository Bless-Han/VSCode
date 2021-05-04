#include <iostream>
#include <array>
using namespace std;
const int N{3};
struct mark{
  array<double, N> a;
  void average(){
    double sum{};
    for (int i=0; i<N; i++)
      sum += a[i];
    cout << sum / N;
  }
  mark(){
    for (int i=0; i<N; i++)
      cin >> a[i];
  }
};
int main(){
  mark * m = new mark;
  m->average();
  delete m;
  return 0;
}
