"""
Mocking-Anwendungsfall in dieser Domäne:
Die Methode `get_discount_percent` greift in echt auf eine Datenbank zu und ist daher langsam, fehleranfällig und abhängig von externer Infrastruktur.
Für Unit-Tests mocken wir sie, damit wir die Fachlogik der Preisberechnung deterministisch und isoliert prüfen können.
So testen wir nur die Berechnung und nicht Verbindungsprobleme, Datenbestand oder DB-Latenzen.
"""

import unittest
from unittest.mock import patch

from A2.shopping_cart import ShoppingCart


class ShoppingCartMockTests(unittest.TestCase):
    # Die Funktionen getQuantity und get_total_of_item werden gemockt, um die Berechnung der Durchschnittspreise zu isolieren.
    # In der IMplementierung benötigen beide eine gefüllte Liste von Items, um die Berechnung durchzuführen. In diesem Test 
    # wollen wir aber nur die Berechnung der Durchschnittspreise testen, nicht die Logik zum Zählen und Summieren der Items.
    # Dies ist ein sehr einfaches Beispiel, für große Warenkörbe mit vielen Artikeln müsste man jedoch viele Items einzeln hinzufügen

    def setUp(self) -> None:
        self.cart = ShoppingCart()

    def test_get_average_price_of_object_mit_gemockter_quantity_und_summe(self) -> None:      
        with patch.object(self.cart, "get_quantity", return_value=4) as mock_quantity:
            with patch.object(self.cart, "get_total_of_item", return_value=20.0) as mock_total:
                average = self.cart.get_average_price_of_object("Buch")

        self.assertEqual(average, 5.0)
        mock_quantity.assert_called_with("Buch")
        mock_total.assert_called_with("Buch")
        self.assertEqual(mock_quantity.call_count, 2)  # get_quantity wird zweimal aufgerufen: einmal in der if-Bedingung und einmal in der Berechnung

    def test_get_average_price_of_object_ist_null_wenn_quantity_null_ist(self) -> None:
        with patch.object(self.cart, "get_quantity", return_value=0) as mock_quantity:
            with patch.object(self.cart, "get_total_of_item", return_value=20.0) as mock_total:
                average = self.cart.get_average_price_of_object("Buch")

        self.assertEqual(average, 0.0)
        mock_quantity.assert_called_with("Buch")
        mock_total.assert_not_called()


if __name__ == "__main__":
    unittest.main()
