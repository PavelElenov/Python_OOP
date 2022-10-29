from project.shopping_cart import ShoppingCart
import unittest

from unittest import TestCase


class ShoppingCartTests(TestCase):
    def test_init(self):
        self.shoppingCart = ShoppingCart('Jumbo', 120.0)

        self.assertEqual('Jumbo', self.shoppingCart.shop_name)
        self.assertEqual(120.0, self.shoppingCart.budget)
        # self.assertEqual({}, self.shoppingCart.products)

        with self.assertRaises(ValueError) as ve:
            self.shoppingCart.shop_name = 'My123magazine'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.shoppingCart.shop_name = 'buy best'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.shoppingCart.add_to_cart('sirene', 100)
        self.assertEqual("Product sirene cost too much!", str(ve.exception))

        result = self.shoppingCart.add_to_cart('sirene', 50)
        self.assertEqual("sirene product was successfully added to the cart!", result)
        self.assertEqual({'sirene': 50}, self.shoppingCart.products)
        result = self.shoppingCart.add_to_cart('coffee', 80)
        self.assertEqual("coffee product was successfully added to the cart!", result)
        self.assertEqual({'sirene': 50, 'coffee': 80}, self.shoppingCart.products)

        with self.assertRaises(ValueError) as ve:
            self.shoppingCart.remove_from_cart('cheese')
        self.assertEqual("No product with name cheese in the cart!", str(ve.exception))

        result = self.shoppingCart.remove_from_cart('sirene')
        self.assertEqual("Product sirene was successfully removed from the cart!", result)
        self.assertEqual({'coffee': 80}, self.shoppingCart.products)

        self.shoppingCart.add_to_cart('sirene', 50)

        with self.assertRaises(ValueError) as ve:
            self.shoppingCart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 10.00lv!", str(ve.exception))

        self.shoppingCart.budget = 200

        result = self.shoppingCart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 130.00lv.', result)

        shoppingcart2 = ShoppingCart('Kaufland', 100)
        shoppingcart2.add_to_cart('cola', 2)

        new_object = self.shoppingCart.__add__(shoppingcart2)
        self.assertEqual('JumboKaufland', new_object.shop_name)
        self.assertEqual(300, new_object.budget)
        self.assertEqual({'sirene': 50, 'coffee': 80, 'cola': 2}, new_object.products)


if __name__ == '__main__':
    unittest.main()
