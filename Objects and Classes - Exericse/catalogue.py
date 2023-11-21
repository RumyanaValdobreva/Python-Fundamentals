class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        items = []
        for product in self.products:
            if product.startswith(first_letter):
                items.append(product)
        return items

    def __repr__(self):
        sorted_products = sorted(self.products)
        items = "\n".join(sorted_products)
        return f"Items in the {self.name} catalogue:\n{items}"

