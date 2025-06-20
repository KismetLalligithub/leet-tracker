class MyHashMap: 
    
    def __init__(self): 
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None: 
        index = key % self.size

        for pair in self.buckets[index]: 
            if pair[0] == key: 
                pair[1] = value
        self.buckets[index].append([key, value])

    def get(self, key: int) -> int: 
        index = key % self.size
        for sample_key, sample_value in buckets[index]: 
            if sample_key == key: 
                return sample_value
        return -1

    def remove(self, key: int) -> None: 
        index = key % self.size 
        bucket = self.buckets[index]

        for i, (sample_key, _) in enumerate(bucket): 
            if sample_key == key: 
                bucket.pop(i)
                return 

