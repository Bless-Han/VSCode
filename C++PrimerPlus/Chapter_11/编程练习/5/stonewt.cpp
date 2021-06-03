#include <iostream>
using std::cout;
#include "stonewt.h"

Stonewt::Stonewt(double lbs)
{
    stone = int (lbs) / Lbs_per_stn;
    pds_left = int (lbs) % Lbs_per_stn + lbs - int(lbs);
    pounds = lbs;
    mode = STONE;
}

Stonewt::Stonewt(int stn, double lbs)
{
    stone = stn;
    pds_left = lbs;
    pounds = stn * Lbs_per_stn + lbs;
    mode = STONE;
}

Stonewt::Stonewt()
{
    stone = pounds = pds_left = 0;
    mode = STONE;
}

Stonewt::~Stonewt()
{
}

// void Stonewt::show_stn() const
// {
//     cout << stone << " stone, " << pds_left << " pounds\n";
// }

// void Stonewt::show_lbs() const
// {
//     cout << pounds << " pounds\n";
// }
std::ostream & operator<<(std::ostream & os, const Stonewt & st)
{
    if (st.mode == st.STONE)
        cout << st.stone << " stone, " << st.pds_left << " pounds\n";
    else if (st.mode == st.POUNDS)
        cout << st.pounds << " pounds\n";
    return os;
}