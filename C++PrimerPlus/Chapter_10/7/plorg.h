#ifndef PLORG_H_
#define PLORG_H_
#include <iostream>
#include <cstring>

class Plorg
{
    private:
        static const int N = 20;
        char name[N];
        int ci;
    public:
        Plorg(const char * str = "Plorga", const int c = 50) { strcpy(name, str); ci = c; }
        void reset(const int c) {ci = c;}
        void show() const;
};
#endif