#include <iostream>
using namespace std;
struct applicant {
  char name[30];
  int credit_ratings[3];
};
void f1(applicant * a);
const char * f2(const applicant * al, const applicant * a2);
typedef void (*pf1)(applicant *a);
typedef const char * (*pf2)(const applicant * a1, const applicant * a2);
int main()
{
  applicant app = {"Smith", {2, 4, 8}};
  pf1 p1 = f1;
  p1(&app);
  pf2 p2 = f2;
  p2(&app, &app);
  pf1 ap[5] = {f1, f1, f1, f1, f1};
  for (int i = 0; i < 5; i++)
    ap[i](&app);
  pf2 pa[10] = {p2,p2,p2,p2,p2,p2,p2,p2,p2,p2};
  for (int i = 0; i < 10; i++)
    pa[i](&app,&app);

  return 0;
}
void f1(applicant * a)
{
    cout << "This is f1.\n";
}
const char * f2(const applicant *a1, const applicant *a2)
{
    cout << "This is f2.\n";
    return "jj";
}