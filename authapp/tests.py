from django.test import TestCase
from authapp.models import Signin, Signup


class SigninTestCase(TestCase):
    def setUp(self):
        Signin.objects.create(username="ajay1234", password="112233")

    def test_Signin_info(self):
        s1 = Signin.objects.get(username="ajay1234", password="112233")
        self.assertEqual(s1.get_user(), "ajay1234")
        self.assertEqual(s1.get_pswd(), "112233")


class SignupTestCase(TestCase):
    def setUp(self):
        Signup.objects.create(firstname="ajay", lastname="rechaveni", username="ajay1234", phone_no="9000570984",
                              password="112233", rpsw="112233")

    def test_Signup_info(self):
        s2 = Signup.objects.get(phone_no=9000570984,firstname="ajay")
        self.assertEqual(s2.get_mobile(), 9000570984)
        self.assertEqual(s2.get_name(), "ajay")