from django.urls import reverse, resolve
from django.test import TestCase


class TestCartAddItemUrl(TestCase):

    def test_reverse(self):
        self.assertEqual(
            first='/cart/add-item/',
            second=reverse('cart:add-item', kwargs={})
        )

    def test_resolve(self):
        resolver = resolve(reverse('cart:add-item', kwargs={}))
        self.assertEqual((), resolver.args)
        self.assertEqual({}, resolver.kwargs)
        self.assertEqual('cart', resolver.app_name)
        self.assertEqual('cart', resolver.namespace)