#ifndef GOLF_H
#define GOLF_H
class Golf
{
    private:
        static const int LEN = 40;
        char fullname[LEN];
        int handicap;
        void setGolf();
    public:
        Golf(const char * name, int hc);
        Golf();
        void setHandicap(int hc);
        void showGolf() const;
};
#endif