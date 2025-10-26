#include <iostream>
#include <string>
#include <vector>
using namespace std;

// 表示?表中每???的?构体
struct Node {
    Node* next; // 下一???指向哪???
    string name; // 与????的值

    Node(string name_ = "") : next(NULL), name(name_) { }
};

// ?表示哨兵的??放置在全局范??
Node* nil;

// 初始化
void init() {
    nil = new Node();
    nil->next = nil; // 在初始??下，?nil指向自己(nil)
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
// ???p的默????置?nil
// 因此，?用insert(v)的操作表示?v插入?表的??
void insert(Node* v, Node* p = nil) {
    v->next = p->next;
    p->next = v;
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

    // 生成每???，并?它?逐?插入?表的??
    for (int i = 0; i < (int)names.size(); ++i) {
        // ?建??
        Node* node = new Node(names[i]);

        // ??建的??插入?表的??
        insert(node);

        // ?出每?步?中?表的??
        cout << "step " << i << ": ";
        printList();
    }
}
