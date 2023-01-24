#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(int argc, char *argv[])
{
    node *list = NULL;
    node *tmp = NULL;
    // ini
    for (int i = 1; i < argc; i++)
    {
        tmp = malloc(sizeof(node));
        if (tmp == NULL)
        {
            return 1;
        }
        tmp->number = atoi(argv[i]);
        tmp->next = list;
        list = tmp;
    }
    
    node *ptr = list;
    // print
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr->number);
    }
    
    // free list
    while (ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }
    return 0;
}