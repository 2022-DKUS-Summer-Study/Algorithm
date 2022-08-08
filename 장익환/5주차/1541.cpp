/*
백준 1541, https://www.acmicpc.net/problem/1541
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

// 식을 값의 최소를 구하는 함수
int get_min(string& exp) {
	int ret = 0;				// 반환 값
	int size = exp.size();
	bool no_minus = true;		// 플래그
	int s = 0;					// 피연산자의 시작 인덱스 
	
	// 문자열을 순회하면서 연산자를 찾음
	for (int i = 0; i < size; i++) {
		if (exp[i] == '+' || exp[i] == '-') { 
			if (no_minus) { // 지금까지 - 연산자가 없었다면
				ret += stoi(exp.substr(s, i - s)); // 현재 연산자 앞에 있는 숫자를 반환값에 더함
			}
			else {
				ret -= stoi(exp.substr(s, i - s)); // 현재 연산자 앞에 있는 숫자를 반환값에서 뺌
			}
			s = i + 1; 
			if (exp[i] == '-') { // 현재 연산자가 - 면
				no_minus = false; // 플래그를 변경
			}
		}
	}
	// 마지막 피연산자를 계산
	if (no_minus) { 
		ret += stoi(exp.substr(s, size - s)); 
	}
	else {
		ret -= stoi(exp.substr(s, size - s));
	}

	return ret;
}

int main(void) {
	string express; // 식을 저장할 문자열
	cin >> express;

	cout << get_min(express);
}

