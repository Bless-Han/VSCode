#include <stdio.h>
#include <cs50.h>

typedef struct
{
    string name;
}
item;

item items[5];
int main()
{
    items[0].name = "good";
    for (int i = 0; i < 5; i++)
    {
        printf("%s, bool is %i\n", items[i].name, items[i].name == NULL);
    }
    
}