from django.test import TestCase
from cartapp.models import Cart
class CartappTestCase(TestCase):
    def setUp(self):
        Cart.objects.create(username="ajay",)

    def test_Signin_info(self):
        s1 = Cart.objects.get(username="ajay")
        self.assertEqual(s1.get_usn, "ajay")

