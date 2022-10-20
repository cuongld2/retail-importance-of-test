from django.test import TestCase
from ..models import Item,OrderItem


class TestMyModel(TestCase):

    def test_default_value_item(self):
        item = Item()
        self.assertEqual(
            item.total, 1)

    def test_default_value_order_item(self):
        item = OrderItem()
        self.assertEqual(
            item.quantity, 1)


