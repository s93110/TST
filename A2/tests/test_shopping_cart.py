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

    def test_add_item_increases_total(self) -> None:
        # Vor hinzufügen eines Artikels
        self.assertEqual(len(self.cart.items),0)
        self.assertEqual(self.cart.is_empty(), True)
        self.assertEqual(self.cart.get_total(), 0.0)

        # Test Step
        self.cart.add_item("Buch", 10.0)
        print(self.cart.items)

        # Nach hinzufügen eines Artikels
        self.assertEqual(len(self.cart.items),1)
        self.assertEqual(self.cart.is_empty(), False)
        self.assertEqual(self.cart.get_total(), 10.0)

    def test_add_multiple_items_sums_total(self) -> None:
        # Mehrere Artikel hinzufügen
        self.cart.add_item("Buch", 10.0)
        self.cart.add_item("Stift", 2.5)
        self.cart.add_item("Heft", 5.0)
        print(self.cart.items)

        self.assertEqual(self.cart.get_total(), 17.5)

    def test_get_quantity_of_item(self) -> None:
        # Mehrere Artikel hinzufügen
        self.cart.add_item("Buch", 10.0)
        self.cart.add_item("Buch", 10.0)
        self.cart.add_item("Stift", 2.5)
        self.cart.add_item("Heft", 5.0)
        self.cart.add_item("Buch", 10.0)

        # Nach hinzufügen von Artikeln
        self.assertEqual(len(self.cart.items), 5)
        self.assertEqual(self.cart.get_quantity("Buch"), 3)


    def test_remove_item(self) -> None:
        # Mehrere Artikel hinzufügen
        self.cart.add_item("Buch", 10.0)
        self.cart.add_item("Stift", 2.5)
        self.cart.add_item("Heft", 5.0)

        # Nach hinzufügen von Artikeln
        self.assertEqual(len(self.cart.items), 3)
        self.assertEqual(self.cart.get_total(), 17.5)

        # Artikel entfernen
        self.cart.remove_item("Stift")

        # Nach entfernen eines Artikels
        self.assertEqual(len(self.cart.items), 2)
        self.assertEqual(self.cart.get_total(), 15.0)
        self.assertEqual(self.cart.get_quantity("Stift"), 0)


if __name__ == "__main__":
    unittest.main()