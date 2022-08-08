/*
백준 13975번, https://www.acmicpc.net/problem/13975
*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 최소 비용을 계산하는 함수
long long get_min_cost(vector<int>& files) {
	priority_queue <long long , vector<long long>, greater<long long>> pq; 
	
	// 우선순위 큐에 파일의 크기를 저장
	int size = files.size();
	for (int i = 0; i < size; i++) {
		pq.push(files[i]); 
	}

	// 크기가 가장 작은 두 파일을 연속해서 합쳐나가면서 최소 비용을 계산
	long long total_cost = 0;
	while (pq.size() != 1) { // 큐에 있는 파일이 하나가 되면 종료
		long long file1 = pq.top();
		pq.pop();
		long long file2 = pq.top();
		pq.pop();
		
		long long cost = file1 + file2;
		total_cost += cost;

		pq.push(cost);
	}

	return total_cost;
}

int main(void) {
	int T;
	int K;

	// 테스트 케이스마다 입력 처리
	cin >> T;
	while (T > 0) {
		vector<int> v;
		cin >> K;
		for (int k = 0; k < K; k++) {
			int temp;
			cin >> temp;
			v.push_back(temp);
		}

		cout << get_min_cost(v) << "\n";
		
		T--;
	}	

	return 0;
}

