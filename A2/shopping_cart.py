class ShoppingCart:
    def __init__(self):
        self.items = []
        self.empty = True
        self.total = 0.0

    def get_total(self) -> float:
        return self.total
    
    def is_empty(self) -> bool:
        return self.empty
    
    def add_item(self, item_name: str, price: float) -> None:
        self.items.append((item_name, price))
        self.total += price
        self.empty = False

    def get_quantity(self, item_name: str) -> int:
        pass