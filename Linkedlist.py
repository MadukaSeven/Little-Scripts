class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = Node()

    def append(self,x:int):
        new_node = Node(x)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = new_node

    def viewLlist(self):
        current = self.head
        ints = []
        while current.next != None:
            current = current.next
            ints.append(current.data)
        return ints
        
    def get_length(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next
        return count
    
    def get(self,index):
        if index >= self.get_length():
            raise Exception("Out of bounds")
        else:
            count = 0
            current = self.head
            while count < index:
                current = current.next
                count += 1
            return current.data
        
    def erase(self,index):
        if index >= self.get_length():
            raise Exception("Out of bounds")
        if index == 0:
            self.head = self.head.next
            return 
        count = 0
        current = self.head
        while count != index:
            last_node = current
            current = current.next
            count += 1
        last_node.next = current.next
