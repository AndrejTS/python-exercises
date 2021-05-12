class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        self.card_num = self.card_num.replace(' ', '')
        if len(self.card_num) < 2 or self.card_num.isdigit() == False:
            return False
        
        self.card_num = self.card_num[::-1]
        sum = 0
        for i in range(len(self.card_num)):
            if i % 2 == 1:
                number = int(self.card_num[i]) * 2
                if number > 9:
                    number -= 9
                sum += number
            else:
                sum += int(self.card_num[i])  
        return sum % 10 == 0
