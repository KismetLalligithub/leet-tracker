class LRUCache: 
    def __init__(self, capacity): 
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node): 
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node): 
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node): 
        self._remove_node(node)
        self._add_node(node)

    def _pop_last(self): 
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node

    def get(self, key): 
        node = self.cache.get(key)

        if node: 
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key, value): 
        node = self.cache.get(key)

        if node: 
            node.value = value
            self._move_to_head(node)
        else:
            new_node = ListNode(key, value)

            if len(self.cache) >= self.capacity: 
                last_node = self._pop_last()

                del self.cache[last_node.key]

            self.cache[key] = new_node 
            self._add_node(new_node)

class ListNode: 
    def __init__(self, key, value): 
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

