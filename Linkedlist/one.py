class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data)+ ' --> '
            itr = itr.next
        print(listr)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr =itr.next
        return count

    def remove_at(self,index):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid index")
        if index ==0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
    
    def insert_at(self,index,data):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
        count =0
        itr = self.head
        while itr:
            if count== index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1


if __name__ == "__main__":
    li = LinkedList()
    # li.insert_at_beginning(5)
    # li.insert_at_beginning(89)
    # li.insert_at_beginning(9)
    # li.insert_at_end(79)
    # li.insert_at_end(69)
    # li.insert_at_end(59)
    # li.insert_at_end(39)
    li.insert_values(["banana","apple","cherry","mango"])
    # li.get_length()
    # li.remove_at(2)

    li.print()
    # li.remove_at(2)
    # li.print()

    li.insert_at(0,"koyya")
    li.insert_at(3,"Pine")
    li.print()


    # print("Length",li.get_length())