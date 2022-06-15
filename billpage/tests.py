from django.test import TestCase,Client
from django.urls import reverse,resolve
from .views import *
from billpage.views import *
# Create your tests here.
class TestUrls(TestCase):
    def test_yourorder_url_is_resolved(self):
        url=reverse('yourorder')
        print(resolve(url))
        self.assertEquals(resolve(url).func, yourorder)

    def test_buy_url_is_resolved(self):
        url=reverse('buy',args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, buy)

    def test_bill_create_is_resolved(self):
        url=reverse('bill_create')
        print(resolve(url))
        self.assertEquals(resolve(url).func, bill_create)

    def test_productedit_is_resolved(self):
        url=reverse('productedit',args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_edit)

    def test_productupdate_is_resolved(self):
        url=reverse('productupdate',args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_update)
