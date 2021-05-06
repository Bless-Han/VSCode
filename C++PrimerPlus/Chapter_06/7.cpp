#include <iostream>
#include <cctype>
using namespace std;
bool judge(char ch);
int main()
{
    cout << "Enter words (q to quit):\n";
    string tmp;
    char ch;
    int vowels{}, consonants{}, others{};
    while (cin >> tmp && !(tmp.size() == 1 && tmp[0] == 'q')){
        ch = tmp[0];
        if (isalpha(ch))
        {
            if (judge(ch))
                vowels++;
            else
                consonants++;
        }
        else
            others++;
    }
    cout << vowels << " words beginning with vowels\n";
    cout << consonants << " words beginning with consonants\n";
    cout << others << " others\n";

    return 0;
}
bool judge(char ch){
    if (ch == 'a' || ch == 'A'
        || ch == 'e' || ch == 'E'
        || ch == 'i' || ch == 'I'
        || ch == 'o' || ch == 'O'
        || ch == 'u' || ch == 'U')
        return true;
    return false;
}