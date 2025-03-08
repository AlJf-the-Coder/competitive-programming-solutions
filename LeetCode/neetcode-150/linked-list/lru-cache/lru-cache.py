class ListNode:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.list = ListNode(-1, 0)
        self.list.prev = self.list
        self.list.next = self.list


    def get(self, key: int) -> int:
        item = self.map.get(key)
        if not item:
            return -1
        item.prev.next = item.next
        item.next.prev = item.prev
        item.next = self.list.next
        item.prev = self.list
        self.list.next.prev = item
        self.list.next = item
        return item.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.val = value
        else:
            if self.list.val == self.capacity:
                node = self.list.prev
                self.list.prev = node.prev
                self.list.prev.next = self.list
                del self.map[node.key]
                del node
                self.list.val -= 1
            node = ListNode(key, value)
            self.map[key] = node
            self.list.val += 1
        node.next = self.list.next
        node.prev = self.list
        self.list.next.prev = node
        self.list.next = node



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
