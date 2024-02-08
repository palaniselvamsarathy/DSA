class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h]= val
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    def __delitem__(self,key):
        h = self.get_hash(key)
t = HashTable()
t['march 6'] = 130
t['march 12'] = 300
t['dec 8'] = 2810
del t['march 6']
print(t['dec 8'])
print(t['dec 10'])

print(t.arr)