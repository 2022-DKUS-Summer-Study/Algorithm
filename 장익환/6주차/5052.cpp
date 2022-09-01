/*
백준 5052, https://www.acmicpc.net/problem/5052
*/

#include <iostream>
#include <cstring>
using namespace std;

char numbers[10000][15]; // 입력받을 전화번호를 저장

// 트라이 클래스
class TrieNode {
public:
	TrieNode* children[10]; // 자식 포인터
	bool is_end;			// 문자열의 끝인지를 나타냄
	
	// 생성자, 초기화 작업 수행
	TrieNode(){
		for (int i = 0; i < 10; i++) {
			children[i] = NULL;
		}
		is_end = false;
	}

	// 소멸자, 메모리 반환 수행
	~TrieNode() {
		for (int i = 0; i < 10; i++) {
			if(children[i])
				delete children[i];
		}
	}

	// 새로운 문자열을 트라이에 삽입하면서 일관성을 유지하는지 확인해주는 메소드
	bool is_consistent(char* ch, int created_node) {
		if (*ch == '\0') {	// 기저 사례, 문자열의 마지막 문자임
			is_end = true;	
			if (created_node == 0) {	// 만약 노드가 생성된 적이 없다면
				return false;			// 현재 추가한 문자열이 접두어임!
			}
			return true;				// 현재까지 다른 문자열의 접두어가 되는 문자열을 발견하지 못함
		}
		
		int next = *ch - '0';	// 다음 노드의 인덱스를 계산

		if (is_end == true) {	// 새로운 문자열을 추가하는 도중에 문자열의 끝을 만나면
			return false;		// 이전에 추가된 문자열이 접두어임!
		}

		if (children[next] == NULL) {	// 포인터가 NULL이면 새로운 자식을 생성
			children[next] = new TrieNode;
			created_node++;	// 생성된 노드의 수를 증가
		}
		
		return children[next]->is_consistent(ch + 1, created_node);	
	}
};

int main(void) {
	int T;
	cin >> T;

	// 각 테스트 케이스에 대해서 입력을 받아서 해결 
	while (T--) {
		int N;
		cin >> N;
		
		for (int i = 0; i < N; i++) {
			cin >> numbers[i];
		}

		// 함수를 실행
		TrieNode root;
		bool flag = true;	// 일관성이 있는지를 나타내는 플래그
		for (int i = 0; i < N; i++) {
			if (!root.is_consistent(numbers[i], 0)) { 
				flag = false; 
				break;
			}
		}

		if (flag) {	// 일관성이 있다면
			cout << "YES\n";	
		}
		else {		// 일관성이 없다면
			cout << "NO\n";
		}
	}
}

