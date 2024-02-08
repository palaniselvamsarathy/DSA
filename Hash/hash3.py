# Add and get an item from the hash map


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    
    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h]=val
    def get(self,key):
        h=self.get_hash(key)
        return self.arr[h]
t = HashTable()
print(t.add('march 6',130))
# print(t.arr)

print(t.get('march 6'))