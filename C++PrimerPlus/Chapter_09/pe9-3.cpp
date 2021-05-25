#include <iostream>
#include <cstring>
struct chaff
{
    char dross[20];
    int slag;
};
void showChaff(const chaff &);
int main()
{
    char buffer[50];
    chaff * cf = new (buffer) chaff[2];
    strcpy(cf[0].dross, "Smith JJ");
    cf[0].slag = 20;
    strcpy(cf[1].dross, "John KK");
    cf[1].slag = 399;
    for (int i = 0; i < 2; i++)
        showChaff(cf[i]);
    return 0;
}
void showChaff(const chaff & cf)
{
    using std::cout;
    using std::endl;
    cout << "Dross = " << cf.dross << endl;
    cout << "slag = " << cf.slag << endl;
}