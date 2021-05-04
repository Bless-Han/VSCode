#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 100001

struct node{
  int data;
  int next;
}node[MAXN];

int List[MAXN];
int main(){
  int First, n, k;
  cin >> First >> n >> k;
  int Address, Data, Next;
  for (int i=0; i<n; i++){
    cin >> Address >> Data >> Next;
    node[Address].data = Data;
    node[Address].next = Next;
  }

  int j=0;
  int p=First;
  while(p!=-1){
    List[j++] = p;
    p = node[p].next;
  }
  int i = 0;
  for( ; i + k<= j; i += k)
    reverse(&List[i], &List[i + k]);
  for (i=0;i<j-1;i++)
    printf("%05d %d %05d\n", List[i], node[List[i]].data, List[i+1]);
  printf("%05d %d -1\n", List[i], node[List[i]].data);
  return 0;
}
