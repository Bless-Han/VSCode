#include <iostream>
#include "golf.h"
int main()
{
    Golf ann("Ann Birdfree", 24);
    ann.showGolf();
    ann = Golf();
    ann.showGolf();
    ann.setHandicap(55);
    ann.showGolf();
    return 0;
}