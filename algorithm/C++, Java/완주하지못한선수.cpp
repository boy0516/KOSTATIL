// 영찬풀이
//no stl(no hash library)

#include <string>
#include <vector>

using namespace std;

#define MAX_TABLE 200007

struct User
{
    int cnt;
    string key;
    User* next;
    User* prev;
};
User user[MAX_TABLE];

unsigned long hashing(string str)
{
    unsigned long hash = 5318;

    for (unsigned int i = 0; i < str.size(); i++)
    {
        //hashing 알고리즘
        hash = (((hash << 5 ) + hash)+str[i])% MAX_TABLE;
    }

    return hash % MAX_TABLE;
}

int add(string key)
{
    unsigned long h = hashing(key);
    int cnt = MAX_TABLE;

    while (user[h].cnt != 0 && cnt--)
    {
        if (user[h].key == key)
        {
            return h;
        }
        h = (h + 1) % MAX_TABLE;
    }
    // cnt가 0일때 마지막으로 실행
    user[h].key = key;
    return h;
}

struct User *running;

void init(void)
{
    running = nullptr;
    for (int i = 0; i < MAX_TABLE; i++)
    {
        user[i].cnt = 0;
        user[i].next = nullptr;
        user[i].prev = nullptr;  
    }
}

string solution(vector<string> participant, vector<string> completion){
    string answer = "";
    init();
    for (unsigned int i = 0; i < participant.size(); i++){
        int temp = add(participant[i]);
        user[temp].cnt++;
        if (user[temp].cnt > 1)
            continue;
        if (running != nullptr)
            running->prev = &user[temp];
        user[temp].next = running;
        // 선형리스트 같이 주소를 연결
        running = &user[temp];
    }
    for (unsigned int i = 0; i< completion.size(); i++){
        int temp = add(completion[i]);
        user[temp].cnt--;
        if (user[temp].cnt != 0)
            continue;

        // 다음 user의 주소의 prev에 접근 후 이전 user주소값 넣어줌
        if (user[temp].next != nullptr) user[temp].next->prev = user[temp].prev;
        // 이전 user의 주소의 next에 접근 후 다음 user주소값 넣어줌
        if (user[temp].prev != nullptr) user[temp].prev->next = user[temp].next;

        // 위 두 연산을 통해 리스트를 연결할


        if (&user[temp] == running) running = user[temp].next;
        user[temp].next = nullptr;
        user[temp].prev = nullptr;
    }
    if (running != nullptr)
        answer = running->key;

    return answer;
}