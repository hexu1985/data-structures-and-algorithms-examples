#include <iostream>
#include <string>
#include <vector>

using namespace std;

// ���?���C???��?���^
struct Node {
    Node *prev, *next;
    string name; // �O????����

    Node(string name_ = "") :
    prev(NULL), next(NULL), name(name_) { }
};

// ?��ܭ�L��??��m�b�����S??
Node* nil;

// ��l��
void init() {
    nil = new Node();
    nil->prev = nil; 
    nil->next = nil;
}

// ?�X?��?�e
void printList() {
    Node* cur = nil->next; // ??��?��?�l
    for (; cur != nil; cur = cur->next) {
        cout << cur->name << " -> ";
    }
    cout << endl;
}

// �b??p���Z���J??v
void insert(Node* v, Node* p = nil) {
    v->next = p->next;
    p->next->prev = v;
    p->next = v;
    v->prev = p;
}

// ?��??
void erase(Node *v) {
    if (v == nil) return; // �p�Gv�O��L??�A?��?�����ާ@
    v->prev->next = v->next;
    v->next->prev = v->prev;
    delete v; // ?��?�s
}

int main() {
    // ��l��
    init();

    // �Q�n?�ت�??���W?�C��
    // �`�N�A�n?�̦Z�@???("yamamoto")?�l�v??�J
    vector<string> names = {"yamamoto",
                            "watanabe",
                            "ito",
                            "takahashi",
                            "suzuki",
                            "sato"};

    // ?��?��G�ͦ��C???�}?�䴡�J?��??
    Node *watanabe;
    for (int i = 0; i < (int)names.size(); ++i) {
        // ?��??
        Node* node = new Node(names[i]);

        // ??�ت�??���J?��??
        insert(node);

        // �O�d"watanabe"??
        if (names[i] == "watanabe") watanabe = node;
    }

    // ?��"watanabe"??
    cout << "before: ";
    printList(); // ?�X?���e��??
    erase(watanabe);
    cout << "after: ";
    printList(); // ?�X?���Z��??
}
