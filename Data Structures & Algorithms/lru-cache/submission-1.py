class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.tbl = {}
        self.cap = capacity
        self.nums = 0
        self.l = ListNode()
        self.r = ListNode()

        self.l.next = self.r
        self.r.prev = self.l

    def get(self, key: int) -> int:
        if key in self.tbl:
            key, val = self.tbl[key].val
            self.pop_node(key)
            self.push_node(key, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.tbl:
            self.push_node(key, value)
            self.nums += 1
        else:
            self.pop_node(key)
            self.push_node(key, value)

        if self.nums > self.cap:
            # pop last one
            last_node = self.r.prev
            k, v = last_node.val
            self.pop_node(k)
            self.nums -= 1

    def pop_node(self, key: int) -> None:
        if key not in self.tbl:
            return
        node = self.tbl[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.tbl[key]

    def push_node(self, key: int, value: int) -> None:
        node = ListNode((key, value), self.l.next, self.l)
        self.l.next.prev = node
        self.l.next = node
        self.tbl[key] = node        
