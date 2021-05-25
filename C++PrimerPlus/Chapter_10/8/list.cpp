#include <iostream>
#include "list.h"
// enum { MAX = 10};
// Item items[MAX];
// int top;
void List::add(Item i)
{
    if (!isfull())
        items[top++] = i;
    else
        std::cout << "Full!!" << std::endl;
}
void List::visit(void (*pf)(Item &))
{
    for (int i = 0; i < top; i++)
        (*pf)(items[i]);
}