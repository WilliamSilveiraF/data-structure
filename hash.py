
class Hash:
    def __init__(self, m):
        self.m = m
        self.queue = [-1] * m

    def hash_s(self, word):
        return len(word) % self.m

    def insert(self, word):
        idx = self.hash_s(word)
        
        while not self.is_empty(idx):
            if self.m - 1 == idx:
                idx = 0
            else:
                idx += 1
        self.queue[idx] = word

    def remove(self, word):
        idx = self.queue.index(word)
        self.queue[idx] = -2

    def is_empty(self, idx):
        return self.queue[idx] == -1 or self.queue[idx] == -2



m = input()
hash_table = Hash(int(m))

while True:
    action = int(input())
    if action == -1:
        break
    word = input()

    if action == 0:
        hash_table.insert(word)
    elif action == 1:
        hash_table.remove(word)

for word in hash_table.queue:
    print(word)

