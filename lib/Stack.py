class Stack:

    def __init__(self, items = [], limit = 100):
        
        self.items = items 
        self.limit = limit
         

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):  
        if not self.full():
           return self.items.append(item)
        else:
            return "is full"      
            

    def pop(self):
        if self.isEmpty() == 0 :
           return self.items.pop()
        else:
            return None

    def peek(self):        
        return self.items[-1]
        
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1

