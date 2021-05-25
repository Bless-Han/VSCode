#ifndef BANK_H_
#define BANK_H_
#include <iostream>

class Bank
{
    private:
        std::string name;
        int number;
        double money;
    public:
        Bank(std::string str, int num = 0, double m = 0.0);
        ~Bank();
        void show() const;
        void put(double m);
        void get(double m);
};
#endif