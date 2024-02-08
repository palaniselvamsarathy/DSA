class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        print( h%self.MAX)
    
t = HashTable()
t.get_hash("Sarathy")
t.get_hash("Sathish")
t.get_hash("march 6")