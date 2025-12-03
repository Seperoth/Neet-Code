class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity
        
    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[i]

arr = DynamicArray(5)

print("Capacity: ", arr.capacity)

print("Size: ", arr.size)

print("Internal Array: ", arr.array)