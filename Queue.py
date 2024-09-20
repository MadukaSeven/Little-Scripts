class Queue:

    def __init__(self,num=5):
        self.array = [None] * num
        self.p1 = 0
        self.p2 = 0
        self.num = num 
        self.size = 0 

    def enqueue(self,x:int):
        if self.size < self.num:
            self.array[self.p1] = x
            self.p2 = (self.p2 + 1) % self.num
            self.size += 1
        else:
            raise Exception("Queue Full")


    def dequeue(self):
        if self.size > 0:
            item = self.array[self.p1] 
            self.p1 = (self.p1 + 1) % self.num
            self.size -= 1
            return item
        else:
            raise Exception("Queue Empty")
        

        
    
    def peek(self):
        if self.size == 0:
            raise Exception("Queue Empty")
        else:    
            return self.array[self.p1]
    
    def isEmpty(self):
        
        return self.size == 0  


    def isFull(self):
        return self.size == self.num
        
    def get_cur_size(self):
        return self.size
