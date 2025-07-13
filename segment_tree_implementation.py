class SegmentTree: 
    def __init__(self, arr): 
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end): 
        if start == end: 
            self.tree[node] = arr[start]
        else: 
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2 

            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, node, start, end, idx, val): 
        if start == end: 
            self.tree[node] = val
        else: 
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2 

            if idx <= mid: 
                self.update(left_child, start, mid, idx, val)
            else: 
                self.update(right_child, mid + 1, end, idx, val)

    def query(self, node, start, end, l, r): 
        if r <  start or l > end: 
            return 0 

        if l <= start and end <= r: 
            return self.tree[node]

        mid = (start + end) // 2
        left_child = 2 * node + 1 
        right_child = 2 * node + 2 

        left_sum = self.query(left_child, start, mid, l, r)
        right_sum = self.query(right_child, mid + 1, end, l , r)
        
        return left_sum + right_sum

    def update_public(self, idx, val): 
        self.update(0, 0, self.n - 1, idx, val)

    def range_sum(self, l, r): 
        return self.query(0, 0, self.n - 1, l, r)
