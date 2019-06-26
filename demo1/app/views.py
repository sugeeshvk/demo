from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.models import manage
from app.forms import manageforms

def logout(request):
        try:
                del request.session['username1']['type']
        except:
                pass
        return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def add(request):
    return render(request,'add.html')

def savelog(request):
    mang=manage()
    if request.method=='POST':
        mang.username=request.POST.get('name')
        mang.password=request.POST.get('pass')
        mang.types=request.POST.get('type')
        mang.save()
        return redirect('/index')

def view(request):
    mang = manage.objects.all()  
    return render(request,"view.html",{'mang':mang }) 

def validlog(request):
        if request.method=='POST':
                ma=manageforms(data=request.POST)
                maa=manage.objects.all()
                use=request.POST.get('uname')
                passs=request.POST.get('upass')
                flag=0
                for aaa in maa:
                        if use==aaa.username and passs==aaa.password:
                                type=aaa.types
                                request.session['username1'] = aaa.username
                                flag=1
                                if type=="admin":
                                        request.session['type'] = aaa.types
                                        return render(request,'adview.html')
                                elif type=="user":
                                        return HttpResponse("user")
                        if flag==0:
                                return HttpResponse("no entry")