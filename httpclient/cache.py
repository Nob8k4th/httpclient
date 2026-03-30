from collections import OrderedDict

class ResponseCache:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.store=OrderedDict()
    def get(self,key):
        if key in self.store:
            self.store.move_to_end(key)
            return self.store[key]
        return None
    def set(self,key,val):
        if key in self.store:
            self.store.move_to_end(key)
        self.store[key]=val
