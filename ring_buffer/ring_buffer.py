class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_ind = 0
        self.length = 0

    def append(self, item):
        # if length is less than the capacity
        if self.length < self.capacity:
            # can just append the item to the end
            self.storage.append(item)
            # increment length by 1
            self.length += 1 
        # if the length is equal to the capacity
        elif self.length == self.capacity:
            # need to remove the oldest value & add new item to it's position/index
            self.storage[self.oldest_ind] = item
            # update oldest value
            self.oldest_ind = (self.oldest_ind + 1) % self.capacity

    def get(self):
        # should be able to just return self.storage here
        return self.storage