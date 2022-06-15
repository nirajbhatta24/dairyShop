from django.test import TestCase,Client
from django.urls import reverse,resolve
from .views import *
from customer.urls import *
# Create your tests here.
class TestUrls(TestCase):
    def test_register_url_is_resolved(self):
        url=reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)



    def test_index_is_resolved(self):
        url=reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_signout_is_resolved(self):
        url=reverse('signout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signout)

    def test_profile_is_resolved(self):
        url=reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)
    
    def test_customer_update_is_resolved(self):
        url=reverse('customer_update',args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func, update)
