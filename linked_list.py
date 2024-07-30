class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList:


    def __init__(self):
        self.head = None
    
    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    def get_length(self):
        c = 0
        itr = self.head
        while itr:
            c+=1
            itr = itr.next
        return c
    
    def remove_at(self, index):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        
        c = 0
        itr = self.head
        while itr:
            if c == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            c += 1
    
    def insert_at(self, index, data):
        if index == 0:
            self.insert_at_begin(data)
            return
        
        c = 0
        itr = self.head
        while itr:
            if c == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            c +=1
    
    def insert_after_value(self, val, d):
        c = 0
        itr = self.head
        while itr:
            if itr.data == val:
                node = Node(d, itr.next)
                itr.next = node
                break
                
            itr = itr.next
            c += 1
        
        if c == self.get_length():
            raise Exception("No such value")
    
    def remove_by_value(self, val):
        c = 0
        itr = self.head
        while itr:
            if itr.data == val:
                self.remove_at(c)
                break
            
            itr = itr.next
            c += 1
        
        if c > self.get_length():
            raise Exception("No such value")

if __name__ == "__main__":
    # ll= LinkedList()
    # # ll.insert_at_begin(5)
    # # ll.insert_at_begin(10)
    # # ll.insert_at_end(20)
    # # ll.insert_at_end(30)
    # ll.insert_values([1,2,3,4])
    # #print(ll.get_length())
    # ll.print()
    # #ll.insert_after_val(5, 33)
    # ll.delete_by_val(5)
    # #ll.remove_at(3)
    # #ll.insert_at(3, 55)
    # ll.print()

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
