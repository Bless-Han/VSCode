#include <iostream>
#include <cstring>
#include "person.h"

// std::string lname;
// char fname[LIMIT];

Person::Person(const std::string & ln, const char * fn)
{
    lname = ln;
    strcpy(fname, fn);
}
void Person::Show() const
{
    std::cout << "Name: " << fname << " " << lname << std::endl;
}
void Person::FormalShow() const
{
    std::cout << "Name: " << lname << " " << fname << std::endl;
}