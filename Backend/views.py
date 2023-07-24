from django.shortcuts import render, redirect
from Backend.models import categorydb, productdb
from Frontend.models import cartDB, cartdetails
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def indexpage(request):
    return render(request, "index.html")


def categorypage(request):
    return render(request, "addcategory.html")


def savecategory(request):
    if request.method == "POST":
        na = request.POST.get('name')
        img = request.FILES['image']
        dsp = request.POST.get('description')
        obj = categorydb(Name=na, Image=img, Description=dsp)
        obj.save()
        return redirect(categorypage)


def displaycategory(request):
    data = categorydb.objects.all()
    return render(request, "displaycategory.html", {'data': data})


def editcategory(request, dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(request, "editcategory.html", {'data': data})


def updatecategory(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        dsp = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Name=na, Description=dsp, Image=file)
        return redirect(displaycategory)


def deletecategory(request, dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)


def productpage(request):
    data = categorydb.objects.all()
    return render(request, "addproduct.html", {'data': data})


def productsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        au = request.POST.get('author')
        la = request.POST.get('language')
        pr = request.POST.get('price')
        pg = request.POST.get('pages')
        ct = request.POST.get('category')
        img = request.FILES['image']
        dsp = request.POST.get('description')
        obj = productdb(Name=na, Author=au, Language=la, Price=pr, Pages=pg, Category=ct, Image=img, Description=dsp)
        obj.save()
        return redirect(productpage)


def productdisplay(request):
    data = productdb.objects.all()
    return render(request, "displayproduct.html", {'data': data})


def editproduct(request, dataid):
    data = productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    return render(request, "editproduct.html", {'data': data, 'da': da})


def updateproduct(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        au = request.POST.get('author')
        la = request.POST.get('language')
        pr = request.POST.get('price')
        pg = request.POST.get('pages')
        ct = request.POST.get('category')
        dsp = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Name=na, Author=au, Language=la, Price=pr, Pages=pg, Category=ct,
                                                   Image=file, Description=dsp)
        return redirect(productdisplay)


def deleteproduct(request, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(productdisplay)


def displaycart(request):
    data = cartDB.objects.all()
    return render(request, "displaycart.html", {'data': data})


def cartcustomerdisplay(request):
    data = cartdetails.objects.all()
    return render(request, "cartcustomerdisplay.html", {'data': data})
