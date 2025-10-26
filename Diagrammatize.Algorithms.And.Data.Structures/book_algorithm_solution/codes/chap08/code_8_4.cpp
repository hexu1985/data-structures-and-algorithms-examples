#include <iostream>
#include <string>
#include <vector>
using namespace std;

// ���?���C???��?���^
struct Node {
    Node* next; // �U�@???���V��???
    string name; // �O????����

    Node(string name_ = "") : next(NULL), name(name_) { }
};

// ?��ܭ�L��??��m�b�����S??
Node* nil;

// ��l��
void init() {
    nil = new Node();
    nil->next = nil; // �b��l??�U�A?nil���V�ۤv(nil)
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
// ???p���q????�m?nil
// �]���A?��insert(v)���ާ@���?v���J?��??
void insert(Node* v, Node* p = nil) {
    v->next = p->next;
    p->next = v;
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

    // �ͦ��C???�A�}?��?�v?���J?��??
    for (int i = 0; i < (int)names.size(); ++i) {
        // ?��??
        Node* node = new Node(names[i]);

        // ??�ت�??���J?��??
        insert(node);

        // ?�X�C?�B?��?��??
        cout << "step " << i << ": ";
        printList();
    }
}
