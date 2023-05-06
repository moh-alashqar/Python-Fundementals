import uuid
class product:
    def __init__(self, name, price, category):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
        self.category = category
    
    def print_info(self):
        print(f"ID: {self.id} Name: {self.name}, Price: {self.price} USD, Category: {self.category}")
        return self

    def update_price(self, percent_change, is_increased):
        if is_increased: 
            self.price *= 1 + percent_change
        else: 
            self.price *= 1 - percent_change
        return self
