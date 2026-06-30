from pathlib import Path
import sys
import unittest
from shopping_cart import ShoppingCart

class ShoppingCartTests(unittest.TestCase):

    def setUp(self):
        # Runs before every test
        self.cart = ShoppingCart()
    
    def test_empty_cart_has_zero_total(self) -> None:
        self.assertEqual(len(self.cart.items),0)
        self.assertEqual(self.cart.is_empty(), True)
        self.assertEqual(self.cart.get_total(), 0.0)

if __name__ == "__main__":
    unittest.main()