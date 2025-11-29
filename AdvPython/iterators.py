## Range Iterator ##
class RangeIterator():
    
    def __init__(self, start_value,limit):
        
        self.start_value = start_value
        self.limit = limit
        
    def __iter__(self):
      return self
  
    def __next__(self):
        
      if self.start_value > self.limit:
          raise StopIteration
      
      temp = self.start_value
      self.start_value += 1
      return temp
  
e = RangeIterator(5,12)

print(next(e))
print(next(e))


## Reverse Iterator##
class ReverseIterator():
    
    def __init__(self, start_value,limit):
        
        self.start_value = start_value
        self.limit = limit
        
    def __iter__(self):
      return self
  
    def __next__(self):
        
      if self.start_value < self.limit:
          raise StopIteration
      
      temp = self.start_value
      self.start_value -= 1
      return temp
  
e = ReverseIterator(12, 5)

print(next(e))
print(next(e))