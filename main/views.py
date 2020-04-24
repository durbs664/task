from django.shortcuts import render, redirect

from .models import *
from .forms import *


#add sp

def add_sp(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method =='POST':
                form    = ServiceP_Form(request.POST, request.FILES )
                # print(form)
                if form.is_valid():
                    print("done")
                #validation,COMMIT=FALSE
                    form.save()
                    form = ServiceP_Form()
                    return redirect("main:home")
            else:
                form = ServiceP_Form()
                print("else")
            return render(request, 'addsp.html', {'form':form})
        return redirect("main:home")
    return redirect("login")

def home(request):
    allsp = Service_Provider.objects.all()
    context = {
        "sp" : allsp,
    }
    return render(request, 'index.html', context)

#detail_view

def detail(request, id):
    if request.user.is_authenticated:
        sp      = Service_Provider.objects.get(id=id)#select * from sp where
        context = {
            "sp":sp
        }
        return render(request, 'details.html', context)
    return redirect("login")

def edit_sp(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            #get the required sp
            sp = Service_Provider.objects.get(id=id)
            if request.method == "POST":
                form = ServiceP_Form( request.POST or None, instance=sp)
                # check validation of form
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:detail", id)
            else:
                form = ServiceP_Form(instance=sp)
            return render(request, 'addsp.html', {"form":form})
        return redirect("main:home")
    return redirect("login")


def delete_sp(request, id):
    sp = Service_Provider.objects.get(id=id)
    sp.delete()
    return redirect("main:home")

def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}

    if request.POST:
        form = AccountUpdate