def maxDistance(s, k): 
    return max(self.flips(s, k, 'NE'), self.flips(s, k, 'NW'), self.flips(s, k, 'SE'), self.flips(s, k, 'sw'))
    
    def flip(s, k, direction):
        res = 0 
        pos = 0 
        opposite = 0 

        for c in s: 
            if c in direction: 
                pos += 1
            else: 
                pos -= 1
                opposite += 1 

            res = max(res, pos + 2 * min(k, opposite))

        return res
