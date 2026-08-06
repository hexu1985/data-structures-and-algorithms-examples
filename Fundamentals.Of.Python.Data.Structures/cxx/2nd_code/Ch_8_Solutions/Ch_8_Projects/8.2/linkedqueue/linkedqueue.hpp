#pragma once

#include <stdexcept>
#include <utility>

template <typename T>
class LinkedQueue {
private:
    // Node structure for singly linked list
    struct Node {
        T data;
        Node* next=nullptr;

        Node(const T& item, Node* nextNode = nullptr)
            : data(item), next(nextNode) {}
    };

    Node* _front=nullptr;
    Node* _rear=nullptr;
    size_t _size=0;

public:
    // Constructor
    LinkedQueue() : _front(nullptr), _rear(nullptr), _size(0) {}

    // Copy constructor
    LinkedQueue(const LinkedQueue& other) = delete;

    // Move constructor
    LinkedQueue(LinkedQueue&& other) = delete;

    // Destructor
    ~LinkedQueue() {
        clear();
    }

    // Copy assignment
    LinkedQueue& operator=(const LinkedQueue& other) = delete;

    // Move assignment
    LinkedQueue& operator=(LinkedQueue&& other) = delete;

    // Check if queue is empty
    bool isEmpty() const {
        return _size == 0;
    }

    // Get current size
    size_t size() const {
        return _size;
    }

    // Peek at front element
    const T& peek() const {
        if (isEmpty()) {
            throw std::runtime_error("The queue is empty.");
        }
        return _front->data;
    }

    // Add element to rear
    void add(const T& item) {
        Node* newNode = new Node(item);
        if (isEmpty()) {
            _front = newNode;
        } else {
            _rear->next = newNode;
        }
        _rear = newNode;
        _size += 1;
    }

    // Remove and return front element
    T pop() {
        if (isEmpty()) {
            throw std::runtime_error("The queue is empty.");
        }
        Node* oldFront = _front;
        T oldData = std::move(_front->data);
        _front = _front->next;
        if (_front == nullptr) {
            _rear = nullptr;
        }
        delete oldFront;
        _size -= 1;
        return oldData;
    }

    // Clear the queue
    void clear() {
        Node* node = _front;
        Node* next = nullptr;
        while (node != nullptr) {
            next = node->next;
            delete node;
            node = next;
        }
        _front = nullptr;
        _rear = nullptr;
        _size = 0;
    }
};
