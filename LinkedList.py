class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

class LinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def insert(self, value):
        new_node = Node(value)

        if self.isEmpty:
            new_node._next = new_node
        else:
            new_node._next = self.tail._next
            self.tail._next = new_node
        self.tail = new_node
        self.size += 1

    @property
    def isEmpty(self):
        return not self.size

    @property
    def length(self):
        return self.size

    @property
    def head(self):
        return self.tail._next

    def prnt(self):
        ref = self.tail._next

        while ref is not self.tail:
            print(ref._value, end=' ')
            ref = ref._next
        print(self.tail._value)

tests_amt = int(input())

def solving(people_amt, size_step):
    my_list = LinkedList()
    for person in range(1, people_amt+1):
        my_list.insert(person)
    
    ref = my_list.head
    while people_amt > 1:
        for _ in range(1, size_step):
            ref = ref._next
        if size_step % people_amt == 0:
            ref = ref._next
        ref._next = ref._next._next
        ref = ref._next
        people_amt -= 1
    return ref._value

while tests_amt:
    people_amt = int(input())
    size_step = int(input())

    res = solving(people_amt, size_step)

    print(f"Using n={people_amt}, m={size_step}, result={res}")

    tests_amt -= 1