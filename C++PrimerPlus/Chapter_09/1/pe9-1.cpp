#include <iostream>
#include "golf.h"
const int N = 50;
int main()
{
    golf ann;
    setgolf(ann, "Ann Birdfree", 24);
    showgolf(ann);
    setgolf(ann);
    showgolf(ann);
    handicap(ann, 55);
    showgolf(ann);
    golf a[N];
    int i = 0;
    std::cout << "While input:\n";
    while(setgolf(a[i++]));
    i--;
    for (int j = 0; j < i; j++)
        showgolf(a[j]);
    return 0;
}