#include <iostream>
#include "move.h"

void Move::showmove() const
{
    std::cout << "x = " << x << std::endl;
    std::cout << "y = " << y << std::endl;
}
Move Move::add(const Move & m) const
{
    Move ret = Move(m.x + this->x, m.y + this->y);
    return ret;
}