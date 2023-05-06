from product import product
class store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product, price, category):
        self.products.append(product(new_product, price, category))

    def sell_product(self, id):
        for i in range(len(self.products)):
            if self.products[i].id == id:
                self.products[i].print_info()
                self.products.pop(i)

    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)

    def all_products_info(self):
        for i in range(len(self.products)):
            self.products[i].print_info()

fruits = store("Fruits")
fruits.add_product("Apple", 1.3, "Fruits")
fruits.add_product("Orange", 2.1, "Fruits")
print("Addition test")
print(fruits.products)
fruits.all_products_info()
print("Selling test")
fruits.sell_product("9d6b33d0-5b97-4c49-b0fc-a93faf050191")
print(fruits.products)
fruits.all_products_info()
fruits.add_product("Apple", 1.3, "Fruits")
print("Updating test")
fruits.products[0].update_price(0.01, True).print_info()
fruits.products[1].update_price(0.02, False).print_info()
fruits.add_product("Tomato", 0.9, "Vegetables")
fruits.add_product("Cucumber", 0.7, "Vegetables")
print("Inflation test")
fruits.inflation(0.01)
fruits.all_products_info()
print("Clearance test")
fruits.set_clearance("Vegetables", 0.01)
fruits.all_products_info()


