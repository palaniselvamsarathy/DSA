class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr = self.head
        while curr.next !=None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.next!=None:
            total +=1
            curr = curr.next
        return total
    
    def display(self):
        elem = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)
    
    def get(self,index):
        if index>=self.length():
            print("ERROR: 'Get' Index out or range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx+=1

    def erase(self,index):
        if index>=self.length():
            print("ERROR: 'Error' Index out or range!")
            return None
        cur = 0
        cur_node = self.head
        while True:
            last= cur_node
            cur_node = cur_node.next
            if cur== index:
                last.next = cur_node.next
                return
            cur+=1


my_list = linked_list()
my_list.display()
my_list.append(12)
my_list.append(14)
my_list.append(16)
my_list.display()

print("Element at index 2:",my_list.get(2))
my_list.get(5)

my_list.erase(1)
my_list.display()