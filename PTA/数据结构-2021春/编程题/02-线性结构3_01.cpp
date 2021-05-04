#include <iostream>
#include <algorithm>
#define MAXN 100001
using namespace std;

struct node{
  int data;
  int next;
}node[MAXN];
int List[MAXN];
int main(void) {
  int first, n, k;
  cin >> first >> n >> k;
  int Address, Data, Next;
  int i=0;
  for (i=0; i<n; i++){
    cin >> Address >> Data >> Next;
    node[Address].data = Data;
    node[Address].next = Next;
  } 
  int j=0;
  int p = first;
  for( ; p != -1; p = node[p].next)
    List[j++] = p;
  for (i = 0; i+k <= j; i+=k)
    reverse(&List[i], &List[i+k]);
  for (i = 0; i<j-1; i++)
    printf("%05d %d %05d\n", List[i], node[List[i]].data, List[i+1]);
  printf("%05d %d -1\n", List[i], node[List[i]].data);
  return 0;
}
