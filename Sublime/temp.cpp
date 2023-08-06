#include <bits/stdc++.h>

using namespace std;

bool f(string s);

int main() {
	#ifndef ONLINE_JUDGE
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif

	int n;
	cin >> n;
	size_t pos;
	string s;
	for (int i = 0; i < n; i++) {
		cin >> s;
		if (f(s))
			cout << "Yes ";
		else
			cout << "No  ";
		cout << s << endl;
	}
}
bool f(string s) {
	size_t pos;
	double a;
	try {
		a = stod(s, &pos);
		if (pos == s.size())
			return true;
	} catch (invalid_argument&) {
		return false;
	}
	return false;
}

