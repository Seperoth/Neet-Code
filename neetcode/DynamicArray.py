class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity


arr = DynamicArray(5)

print("Capacity: ", arr.capacity)

print("Size: ", arr.size)

print("Internal Array: ", arr.array)

print("Adding elements to the dynamic array...")