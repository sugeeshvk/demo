from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from app.models import catogery,product
from app.forms import catogeryForms,productForms

def index(request):
    return render(request,'index.html')

def addproduct(request):
    return render(request,'addproduct.html')

def search(request):
    cat=catogery.objects.all()
    return render(request,'search.html',{'form':cat})

def searchcatogery(request):
    if  request.method=="POST":
        id=request.POST.get('catogery')
        prod = product.objects.filter(l_product=id)  
        return render(request,'se_cat_view.html',{'prod':prod})


def saveproduct(request):
    prod=product()
    cat=catogery()
    if request.method=='POST':
        prod.l_id=request.POST.get('pid')
        prod.l_product=request.POST.get('pproduct')
        prod.l_name=request.POST.get('pname')
        prod.l_price=request.POST.get('pprice')
        prod.save()
        # cat.p_pid=request.POST.get('pid')
        # cat.p_product=request.POST.get('pproduct')
        # cat.p_price=request.POST.get('pprice')
        # cat.save()
        return redirect('/index')