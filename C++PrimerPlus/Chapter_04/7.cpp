#include <iostream>
using namespace std;
const int N = 20;
struct Pizza{
  char name[N];
  double length;
  double weight;
};
int main(){
  Pizza p;
  cin.getline(p.name, 20);
  cin >> p.length >> p.weight;
  cout << p.name << endl 
    << p.length << endl 
    << p.weight << endl;
  return 0;
}
