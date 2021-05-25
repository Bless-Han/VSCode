#include <iostream>
#include "move.h"
int main()
{
    Move m1(2, 6);
    m1.showmove();
    m1.reset(9, 10);
    m1.showmove();
    Move m2 = m1.add(m1);
    m2.showmove();
    return 0;
}