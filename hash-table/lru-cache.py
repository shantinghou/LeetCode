class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def delete(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add(self, node):
        temp = self.back.prev
        temp.next = node
        node.prev = temp
        self.back.prev = node
        node.next = self.back

    def __init__(self, capacity: int):
        self.cache = {}
        self.front = Node(-1, -1)
        self.back = Node(-1, -1)
        self.front.next = self.back
        self.back.prev = self.front
        self.capacity = capacity

    def get(self, key: int) -> int:
        cache = self.cache
        
        if key in cache:
            node = cache[key]
            self.delete(node)
            self.add(node)
            return cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        cache = self.cache
        if key in cache:
            cache[key].value = value
            self.delete(cache[key])
            self.add(cache[key])
        else:
            self.capacity -= 1
            if self.capacity < 0:
                toPop = self.front.next
                self.delete(toPop)
                cache.pop(toPop.key, None)
                self.capacity += 1
            cache[key] = Node(key, value)
            node = cache[key]
            self.add(node)

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)