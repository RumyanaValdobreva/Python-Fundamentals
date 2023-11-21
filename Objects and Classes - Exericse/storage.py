class Storage:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        if self.capacity > 0:
            self.capacity -= 1
            self.storage.append(product)

    def get_products(self):
        return self.storage


