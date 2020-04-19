from django.shortcuts import render, redirect

from .models import Service_Provider
from .forms import ServiceP_Form


#add sp

def add_sp(request):
    if request.method =='POST':
        form    = ServiceP_Form(request.POST, request.FILES )
        print(form)

        if form.is_valid():
            print("done")

        #validation,COMMIT=FALSE
            form.save()
            form = ServiceP_Form()
            return redirect("main:home")
    else:
        form = ServiceP_Form()
        print("else")
    return render(request, 'main/addsp.html', {'form':form})

def home(request):
    allsp = Service_Provider.objects.all()
    context = {
        "sp" : allsp,
    }
    return render(request, 'main/index.html', context)

#detail_view

def detail(request, id):
    sp      = Service_Provider.objects.get(id=id)#select * from sp where
    context = {
        "sp":sp
    }
    return render(request, 'main/details.html', context)

def edit_sp(request, id):
    #get the required movies
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
    return render(request, 'main/addsp.html', {"form":form})

def delete_sp(request, id):
    sp = Service_Provider.objects.get(id=id)
    sp.delete()
    return redirect("main:home")