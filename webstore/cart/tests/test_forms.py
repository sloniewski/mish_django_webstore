from django.test import TestCase

from webstore.cart import forms
from webstore.product.models import Product


class TestAddItemForm(TestCase):
    form_class = forms.AddItemForm

    def setUp(self):
        self.test_product = Product.objects.create(name='The Holy Grail')

    def test_data_validation(self):
        product = Product.objects.create(name='test')
        form = self.form_class({'item': product.pk, 'qty': '5'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = self.form_class({'item': -1, 'qty': 0},)
        form.full_clean()
        self.assertFalse(form.is_valid())
        self.assertIn('no such product', form.errors['item'].as_json())
        self.assertIn('cannot add 0', form.errors['item'].as_json())
        self.assertIn('cannot add 0', form.errors['qty'].as_json())