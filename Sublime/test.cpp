#include <bits/stdc++.h>

using namespace std;

int countDecimalPlaces(string s);

int main() {
	#ifndef ONLINE_JUDGE
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif

	int n;
	cin >> n;
	string s;
	for (int i = 0; i < n; i++) {
		cin >> s;
		cout << s << " -> " << countDecimalPlaces(s) << endl;
	}
}
int countDecimalPlaces(string s) {
	size_t pos = s.find('.');
	if (pos == string::npos)
		return 0;
	return s.size() - pos - 1;
}
