class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(self.size)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
            return hash % self.size
    
    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        self.table[hash] = value
    
    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.table[hash]
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.table[hash] = None

