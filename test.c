#include <stdio.h>
#include <cs50.h>

typedef int integer;

int main()
{
    string s = "Hi!";
    string t = "Hi!";
    if (s == t)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}
