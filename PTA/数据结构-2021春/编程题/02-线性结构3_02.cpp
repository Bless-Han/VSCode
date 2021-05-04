#include <iostream>
#include <algorithm>
#define MAXN 100001
using namespace std;

struct note{
  int data;
  int next;
}note[MAXN];
int List[MAXN];
int main(void) {
  int first, n, k;
  int Address, Data, Next;
  cin >> first >> n >> k;
  for (int i=0; i<n; i++){
    cin >> Address >> Data >> Next;
    note[Address].data = Data;
    note[Address].next = Next;
  }
  int p=first;
  int j=0;
  for ( ; p != -1; p=note[p].next)
    List[j++] = p;
  int i=0;
  for ( ; i+k <= j; i+=k)
    reverse(&List[i], &List[i+k]);
  for (i=0; i<j-1; i++)
    printf("%05d %d %05d\n", List[i], note[List[i]].data, List[i+1]);
  printf("%05d %d -1\n", List[i], note[List[i]].data);
  return 0;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
}
