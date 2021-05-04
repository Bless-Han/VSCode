#include <iostream>
using namespace std;

void mice();
void run();
int main(){
  mice();
  mice();
  run();
  run();
  return 0;
}
void mice(){
  cout << "Three blind mice\n";
}
void run(){
  cout << "See how they run\n";
}
