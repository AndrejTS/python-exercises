class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.oldest_item = 0
        self.buffer = [None for _ in range(capacity)]
        

    def read(self):
        output = ''
        if self.buffer[self.oldest_item] != None:
            output = self.buffer[self.oldest_item]
            self.buffer[self.oldest_item] = None
            self.set_oldest_item()
            return output
        else:
            raise BufferEmptyException('Buffer is empty')


    def write(self, data):
        for i in range(len(self.buffer)):
            index_to_write = (self.oldest_item + i) % len(self.buffer)
            if self.buffer[index_to_write] == None:
                self.buffer[index_to_write] = data
                return
        raise BufferFullException('Buffer is full')


    def overwrite(self, data):
        try:
            self.write(data)
        except:
            self.buffer[self.oldest_item] = data
            self.set_oldest_item()


    def clear(self):
        for i in range(len(self.buffer)):
            self.buffer[i] = None


    def set_oldest_item(self):
        self.oldest_item += 1
        self.oldest_item %= len(self.buffer)

