#include <iostream>
using namespace std;
struct box
{
    char maker[40];
    float height;
    float width;
    float length;
    float volume;
};
void fa(box);
void fb(box *);
int main()
{
    box bb = {"Smith", 2, 4, 9, 5};
    fa(bb);
    fb(&bb);
    fa(bb);
    return 0;
}
void fa(box b)
{
    cout << "maker = " << b.maker << endl;
    cout << "height = " << b.height << endl;
    cout << "width = " << b.width << endl;
    cout << "length = " << b.length << endl;
    cout << "volume = " << b.volume << endl;
}
void fb(box * pb)
{
    pb->volume = pb->height * pb->width * pb->length;
}