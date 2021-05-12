from random import randint


GLOBAL_NAME_CACHE = set()


class Robot:
    def __init__(self):
        self.name = self.new_name()
        

    def new_name(self):
        name = self.generate_name() 
        while name in GLOBAL_NAME_CACHE:
            name = self.generate_name()
        GLOBAL_NAME_CACHE.add(name)
        return name


    @staticmethod 
    def generate_name():
        name = ''
        for _ in range(2):
            name += chr(randint(65, 90))
        for _ in range(3):
            name += chr(randint(48, 57))  
        return name


    def reset(self):
        self.__init__()
