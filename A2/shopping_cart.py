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
        quantity = len([item for item in self.items if item[0] == item_name])
        return quantity
    
    def remove_item(self, item_name: str) -> None:
        for i, item in enumerate(self.items):
            if item[0] == item_name:
                self.total -= item[1]
                del self.items[i]
                break
        if not self.items:
            self.empty = True