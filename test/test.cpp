#include <bits/stdc++.h>

using namespace std;

int add(int a, int b);

int main() {
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

	std::string s;
	getline(cin, s);
    cout << s << endl;
    cout << add(1, 9) << endl;
    cout << add(1, 9) << endl;
}
int add(int a, int b) {return a + b;}
