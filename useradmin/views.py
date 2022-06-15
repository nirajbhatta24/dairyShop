from billpage.models import Buyproduct
from customer.models import Customer
from django.shortcuts import render, redirect
from product.models import Product
from useradmin.forms import UseradminForm
from useradmin.models import Useradmin
def adminDashboard(request):

    if (request.method == "POST"):

        page = int(request.POST['page'])

        if ('prev' in request.POST):

            page = page - 1

        if ('next' in request.POST):

            page = page + 1

        tempOffSet = page - 1

        offset = tempOffSet * 7

        print(offset)

    else:

        offset = 0

        page = 1

    customers=Customer.objects.raw("select * from customer limit 7 offset % s", [offset])

    pageItem = len(customers)

    return render(request, "admin/adminDashboard.html", {'customers': customers, 'page': page, 'pageItem': pageItem})
    
def crudProduct(request):
    
    products=Product.objects.raw('select * from product')
    return render(request,"admin/crudProduct.html",{'products':products})

def customer_delete(request,p_id):
    customer=Customer.objects.get(customer_id=p_id)
    customer.delete()
    return redirect ("/useradmin/adminDashboard")

def deletebill(request,d_id):
    deletebills=Buyproduct.objects.get(buyproduct_id=d_id)
    deletebills.delete()
    return redirect ("/useradmin/billing")

def billing(request):
    bills=Buyproduct.objects.raw('select * from buyproduct')
    return render(request,"admin/billing.html",{'bills':bills})

def userinfo(request):
    if(request.method=="POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page= page-1
        if ('next' in request.POST):
             page=page+1
        tempOffSet = page - 1
        offset=tempOffSet*4
        print(offset)
    else:
        offset=0
        page=1
    users=Useradmin.objects.raw("select * from useradmin limit 4 offset % s",[offset])
    pageItem=len(users)
    return render(request,"admin/viewuser.html",{'users':users,'page':page,'pageItem':pageItem})

def adduser(request):
    if request.method=="POST":
        form=UseradminForm(request.POST)
        print(form)
        if form.is_valid():
            
                print("valid")
                form.save()
                return redirect("/useradmin/userinfo")
         
    else:
        form=UseradminForm()
        print("invalid")
    return render(request, "admin/adduser.html",{'form':form})


def edituser(request,p_id):
    try:
       users=Useradmin.objects.get(id=p_id)
       print(users)
       return render(request, "admin/edituser.html", {'users':users})
    except:
       print("No Data Found")
    return redirect("/useradmin/userinfo")


def updateuser(request,p_id):
    user = Useradmin.objects.get(id=p_id)
    form = UseradminForm(request.POST, instance=user)
    if form.is_valid():
        try:
           form. save()
           return redirect("/useradmin/userinfo")
           
        except:
           print("validation failed")
    return render(request, "admin/edituser.html", {'users':user})


def deleteuser(request,p_id):
    try:
       user=Useradmin.objects.get(id=p_id)
       user.delete()
    except:
        print("No data Found")
    return redirect("/useradmin/userinfo")