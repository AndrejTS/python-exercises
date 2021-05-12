class InputCell:
    def __init__(self, initial_value):
        self.data = initial_value
        self.subscribers = set()

    @property
    def value(self):
        return self.data

    @value.setter
    def value(self, new_value):
        self.data = new_value
        for subscriber in self.subscribers:
            subscriber.update()

    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.comp_func = compute_function
        self.callbacks = set()
        self.data = compute_function([i.value for i in inputs])
        self.subscribe(self)

    @property
    def value(self):
        self.update()
        return self.data

    def subscribe(self, cell):
        for i in self.inputs:
            i.subscribe(cell)

    def update(self):
        old_value = self.data
        self.data = self.comp_func([i.value for i in self.inputs])
        if self.data != old_value:
            for callback in self.callbacks:
                callback(self.data)

    def add_callback(self, callback):
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        self.callbacks.discard(callback)
