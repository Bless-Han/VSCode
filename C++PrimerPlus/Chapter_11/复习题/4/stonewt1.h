#ifndef STONEWT_H_
#define STONEWT_H_
class Stonewt
{
    private:
        enum {Lbs_per_stn = 14};
        int stone;
        double pds_left;
        double pounds;
    public:
        Stonewt(double lbs);
        Stonewt(int stn, double lbs);
        Stonewt();
        ~Stonewt();
        void show_lbs() const;
        void show_stn() const;
        Stonewt operator*(const double & n) const;
        friend Stonewt operator*(double n, const Stonewt & s)
            { return s * n; }
        operator int() const;
        operator double() const;
};
#endif