class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[i]
    
    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = n
        self.size += 1

#   testing
arr = DynamicArray(5)

print("Capacity: ", arr.capacity)

print("Size: ", arr.size)

print("Internal Array: ", arr.array)
