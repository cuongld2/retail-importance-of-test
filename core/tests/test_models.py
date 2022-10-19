from django.test import TestCase
from ..models import Item


class TestMyModel(TestCase):

    def test_experiment_email(self):
        item = Item()
        self.assertEqual(
            item.total, 1)

