class MyHashMap: 
    def __int__(self): 
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key): 
        return key % self.size
    
    def put(self, key, value): 
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        for i, (k, v) in eumerate(bucket): 
            if k == key: 
                bucket[i] = (key, value)
                return 
            
        bucket.append((key, value))

    def get(self, key): 
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for k, v in bucket: 
            if k == key: 
                return v 
            
        return -1 
    

    def remove(self, key): 
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for i, (k, v) in enumerate(bucket): 
            if k == key: 
                del bucket[i]
                return 
