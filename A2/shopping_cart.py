class ShoppingCart:
    def __init__(self):
        self.items = []
        self.empty = True
        self.total = 0.0

    def get_total(self) -> float:
        return self.total
    
    def is_empty(self) -> bool:
        return self.empty