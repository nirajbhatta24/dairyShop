from itertools import product
from django.shortcuts import render,redirect
from product.models import Product
from billpage.models import Buyproduct
from billpage.forms import BuyproductForm
from customer.models import Customer
# Create your views here.
def buy(request,p_id):
    try:
        product=Product.objects.get(product_id=p_id)
        print(product)
        return render(request, "customer/buyPage.html", {'product':product})
    except:
        print("No Data Found")
    return render(request, "customer/buyPage.html")

def bill_create(request):
    if request.method == "POST":
        print(request.POST)
        form = BuyproductForm(request.POST)
        form.save()
        return redirect("/")
    else:
        form = BuyproductForm()
    return render(request, "customer/buyPage.html")



def yourorder(request):
    bills=Buyproduct.objects.filter(customer=request.session['customer_id'])
    users=Customer.objects.get(customer_id=request.session['customer_id'])
    return render(request, "customer/yourorder.html", {'users':[users],'bills':bills})

def product_delete(request,p_id):
    product=Buyproduct.objects.get( buyproduct_id=p_id)
    product.delete()
    return redirect ("/billpage/yourorder")

def product_edit(request,p_id):
    product=Buyproduct.objects.get( buyproduct_id=p_id)
    return render (request, "customer/yourorderedit.html",{'product':product})

def product_update(request,p_id):
    product=Buyproduct.objects.get(buyproduct_id=p_id)
    form=BuyproductForm(request.POST, instance=product)
    form.save()
    #bills=Buyproduct.objects.filter(customer=request.session['customer_id'])
    #users=Customer.objects.get(customer_id=request.session['customer_id'])
    return redirect ("/billpage/yourorder")
