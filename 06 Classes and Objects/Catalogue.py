class Catalogue:
    nl = '\n'

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        stuff = []
        for product in self.products:
            if product[0] == first_letter:
                stuff.append(product)

        return stuff

    def __repr__(self):
        return f"Items in the {self.name} catalogue:\n{Catalogue.nl.join(sorted(self.products))}"