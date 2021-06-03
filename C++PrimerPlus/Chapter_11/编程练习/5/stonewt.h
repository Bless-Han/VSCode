#ifndef STONEWT_H_
#define STONEWT_H_
#include <iostream>

class Stonewt
{
    private:
        enum {Lbs_per_stn = 14};
        enum Mode { STONE, POUNDS};
        Mode mode;
        int stone;
        double pds_left;
        double pounds;
    public:
        Stonewt(double lbs);
        Stonewt(int stn, double lbs);
        Stonewt();
        ~Stonewt();
        void set_stn() { mode = STONE; }
        void set_lbs() { mode = POUNDS; }
        friend std::ostream & operator<<(std::ostream & os, const Stonewt & st);
        // void show_lbs() const;
        // void show_stn() const;
};
#endif