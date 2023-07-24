from django.shortcuts import render, redirect
from Backend.models import categorydb, productdb
from Frontend.models import cartDB, cartdetails, customerdetails
from django.db.models import Sum
from django.contrib import messages


# Create your views here.
def homepage(request):
    data = categorydb.objects.all()
    return render(request, "home.html", {'data': data})


def aboutpage(request):
    data = categorydb.objects.all()
    return render(request, "about.html", {'data': data})


def contactpage(request):
    data = categorydb.objects.all()
    return render(request, "contact.html", {'data': data})


def genrepage(request, itemcatg):
    products = productdb.objects.filter(Category=itemcatg)
    data = categorydb.objects.all()
    return render(request, "genre.html", {'data': data, 'products': products})


def singleproduct(request, dataid):
    data = categorydb.objects.all()
    products = productdb.objects.get(id=dataid)
    return render(request, "singleproduct.html", {'data': data, 'products': products})


def cartpage(request):
    data = cartDB.objects.all()
    grandtotal = data.aggregate(Sum("Totalprice"))["Totalprice__sum"]
    return render(request, "cart.html", {'data': data, 'grandtotal': grandtotal})


def savecart(request):
    if request.method == "POST":
        pna = request.POST.get('productname')
        qty = request.POST.get('quantity')
        tp = request.POST.get('totalprice')
        obj = cartDB(Pname=pna, Quantity=qty, Totalprice=tp)
        obj.save()
        messages.success(request, "Added to cart successfully")
        return redirect(cartpage)


def deletecart(request, dataid):
    data = cartDB.objects.filter(id=dataid)
    data.delete()
    return redirect(cartpage)


def savecartdetails(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ad = request.POST.get('address')
        cty = request.POST.get('country')
        st = request.POST.get('state')
        pc = request.POST.get('postalcode')
        ph = request.POST.get('phoneno')
        em = request.POST.get('email')
        obj = cartdetails(Name=na, Address=ad, Country=cty, State=st, PostalCode=pc, PhoneNo=ph, Email=em)
        obj.save()
        messages.success(request, "Submitted successfully")
        return redirect(cartpage)


def signuppage(request):
    return render(request, "signpage.html")


def savesignup(request):
    if request.method == "POST":
        una = request.POST.get('username')
        em = request.POST.get('email')
        ps = request.POST.get('password')
        cps = request.POST.get('confirmpassword')
        obj = customerdetails(Username=una, Email=em, Password=ps, Confirm_password=cps)
        obj.save()
        return redirect(signuppage)


def userlogin(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if customerdetails.objects.filter(Username=username_r, Password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r
            return redirect(homepage)
        else:
            return redirect(signuppage)
    return redirect(signuppage)


def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('signuppage')
