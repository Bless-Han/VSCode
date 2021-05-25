#ifndef FILE_H_
#define FILE_H_
typedef int Item;

class List
{
    private:
        enum { MAX = 10};
        Item items[MAX];
        int top;
    public:
        List() { top = 0;}
        bool isempty() const {return top == 0;}
        bool isfull() const {return top == MAX;}
        void add(Item i);
        void visit(void (*pf)(Item &));
};
#endif