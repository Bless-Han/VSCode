#ifndef STONEWT_H_
#define STONEWT_H_
#include <iostream>

class Stonewt
{
    public:
        enum Mode { STONE, POUNDS};
    private:
        enum {Lbs_per_stn = 14};
        Mode mode;
        int stone;
        double pds_left;
        double pounds;
    public:
        Stonewt(double lbs, Mode mode = STONE);
        Stonewt(int stn, double lbs, Mode mode = STONE);
        Stonewt(Mode mode = STONE);
        ~Stonewt();
        void set_stn() { mode = STONE; }
        void set_lbs() { mode = POUNDS; }
        bool operator==(const Stonewt & s) const { return pounds == s.pounds; }
        bool operator!=(const Stonewt & s) const { return pounds != s.pounds; }
        bool operator<=(const Stonewt & s) const { return pounds <= s.pounds; }
        bool operator>=(const Stonewt & s) const { return pounds >= s.pounds; }
        bool operator<(const Stonewt & s) const { return pounds < s.pounds; }
        bool operator>(const Stonewt & s) const { return pounds > s.pounds; }
        friend std::ostream & operator<<(std::ostream & os, const Stonewt & st);
        // void show_lbs() const;
        // void show_stn() const;
};
#endif