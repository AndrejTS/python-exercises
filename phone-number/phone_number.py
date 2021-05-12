import string


class PhoneNumber:
    def __init__(self, number):
        self.number = ''
        for i in number:
            if i in string.digits:
                self.number += i
        if len(self.number) == 11 and self.number[0] == '1':
            self.number = self.number[1:]
        if len(self.number) != 10:
            raise ValueError('Error')
        if self.number[0] in '01' or self.number[3] in '01':
            raise ValueError('Error')
        self.area_code = self.number[0:3]
        

    def pretty(self):
        return f"({self.number[0:3]}) {self.number[3:6]}-{self.number[6:]}"
