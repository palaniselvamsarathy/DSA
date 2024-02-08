class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found= False
        for idx, elem in enumerate(self.arr[h]):
            if(len(elem)==2 and elem[0]==key):
                self.arr[h][idx] =(key,val) 
                found = True
                break
            if not found:
                self.arr[h].append((key,val))
                
        
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    def __delitem__(self,key):
        h = self.get_hash(key)

t = HashTable()
t['march 6'] = 120
t['march 10'] = 130
t['march 17'] = 459
t['march 10'] = 130
t['march 8'] = 2810
t['march 12'] = 140
t['dec 13'] =230
t['dec 12'] =530

print(t.get_hash('march 10'))
print(t.get_hash('march 8'))
print(t.get_hash('march 6'))
print(t.get_hash('march 17'))
print(t.get_hash('dec 13'))
print(t.get_hash('dec 12'))
print(t.arr)