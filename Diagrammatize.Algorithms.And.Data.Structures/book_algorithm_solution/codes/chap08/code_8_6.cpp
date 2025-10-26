#include <iostream>
#include <string>
#include <vector>

using namespace std;

// 表示?表中每???的?构体
struct Node {
    Node *prev, *next;
    string name; // 与????的值

    Node(string name_ = "") :
    prev(NULL), next(NULL), name(name_) { }
};

// ?表示哨兵的??放置在全局范??
Node* nil;

// 初始化
void init() {
    nil = new Node();
    nil->prev = nil; 
    nil->next = nil;
}

// ?出?表的?容
void printList() {
    Node* cur = nil->next; // ??表的?部?始
    for (; cur != nil; cur = cur->next) {
        cout << cur->name << " -> ";
    }
    cout << endl;
}

// 在??p之后插入??v
void insert(Node* v, Node* p = nil) {
    v->next = p->next;
    p->next->prev = v;
    p->next = v;
    v->prev = p;
}

// ?除??
void erase(Node *v) {
    if (v == nil) return; // 如果v是哨兵??，?不?行任何操作
    v->prev->next = v->next;
    v->next->prev = v->prev;
    delete v; // ?放?存
}

int main() {
    // 初始化
    init();

    // 想要?建的??的名?列表
    // 注意，要?最后一???("yamamoto")?始逐??入
    vector<string> names = {"yamamoto",
                            "watanabe",
                            "ito",
                            "takahashi",
                            "suzuki",
                            "sato"};

    // ?建?表：生成每???并?其插入?表的??
    Node *watanabe;
    for (int i = 0; i < (int)names.size(); ++i) {
        // ?建??
        Node* node = new Node(names[i]);

        // ??建的??插入?表的??
        insert(node);

        // 保留"watanabe"??
        if (names[i] == "watanabe") watanabe = node;
    }

    // ?除"watanabe"??
    cout << "before: ";
    printList(); // ?出?除前的??
    erase(watanabe);
    cout << "after: ";
    printList(); // ?出?除后的??
}
