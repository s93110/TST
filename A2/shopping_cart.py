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
    
    def get_total_of_item(self, item_name: str) -> float:
        total = sum(item[1] for item in self.items if item[0] == item_name)
        return total
    
    def remove_item(self, item_name: str) -> None:
        for i, item in enumerate(self.items):
            if item[0] == item_name:
                self.total -= item[1]
                del self.items[i]
                break
        if not self.items:
            self.empty = True

    def get_average_price_of_object(self, item_name: str) -> float:
        return self.get_total_of_item(item_name) / self.get_quantity(item_name) if self.get_quantity(item_name)>0 else 0.0
