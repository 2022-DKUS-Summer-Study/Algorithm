/*
백준 16916, https://www.acmicpc.net/problem/16916
*/

#include <iostream>
#include <string>
using namespace std;

// pi 배열을 계산하는 함수
int* get_fail(string& P) {
	int j = 0;
	int m = P.size();
	int* pi = new int[m];
	pi[0] = 0;
	for (int i = 1; i < m; i++) { 
		while (j > 0 && P[i] != P[j]) {
			j = pi[j - 1];
		}
		if (P[i] == P[j]) {
			pi[i] = ++j;
		}
		else {
			pi[i] = 0;
		}
	}

	return pi;
}

// kmp 알고리즘을 구현한 함수
int kmp(string& S, string& P) {
	int j = 0;
	int n = S.size();
	int m = P.size();
	int* pi = get_fail(P);

	for (int i = 0; i <= n; i++) {
		while (j > 0 && S[i] != P[j]) {
			j = pi[j - 1];
		}

		if (S[i] == P[j]) {
			++j;
			if (j == m) {
				return 1;
			}
		}
	}

	return 0;
}

int main(void) {
	string S;
	string P;

	cin >> S;
	cin >> P;

	cout << kmp(S, P);
}

