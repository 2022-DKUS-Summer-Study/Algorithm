/*
백준 1931번, https://www.acmicpc.net/problem/1931
*/

#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

// 정렬을 위해 사용하는 함수
bool compare(pair<int, int> a, pair<int, int> b) {
	// 종료시간을 기준으로 정렬하되, 종료시간이 같으면 시작 시간을 기준으로 정렬
	if (a.second == b.second) {
		return a.first < b.first;
	}
	return a.second < b.second;
}

// 가능한 회의의 최대 개수를 구하는 함수
int get_max(vector<pair<int, int>>& v) {
	int count = 0;		// 반환할 값
	int recent_end = 0;	// 지난번 회의의 종료시간
	int size = v.size();

	// 정렬된 배열을 순회하면서 개최할 수 있는 회의의 수를 구함
	for (int i = 0; i < size; i++) {
		if (v[i].first >= recent_end) { // 시작 시간이 지난번 회의의 종료시간과 같거나 그보다 뒤라면 
			count++;					// 이 회의를 선택
			recent_end = v[i].second;	
		}
	}
	return count;
}

int main(void) {
	int N;
	vector<pair<int, int>> v;

	cin >> N;
	for (int i = 0; i < N; i++) {
		int temp1, temp2;
		cin >> temp1 >> temp2;
		v.push_back(make_pair(temp1, temp2)); // 시작 시간, 종료 시간 쌍을 배열에 저장
	}

	// 배열을 정렬
	sort(v.begin(), v.end(), compare); 
	
	cout << get_max(v);

	return 0;
}

