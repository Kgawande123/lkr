from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person


# Create your views here.
def hview(request):
    return  render(request,"app1/Home.html",{})
def pview(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")

    return render(request,"app1/person.html",{"form":form})

def sview(request):
    per = Person.objects.all()
    return render(request,"app1/show.html",{"per":per})


def uview(request,pk):
    obj = Person.objects.get(pid=pk)
    form = PersonForm(instance=obj)
    if request.method == "POST":
        form = PersonForm(request.POST,instance=obj)

        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/person.html",{"form":form})

def dview(request,k):
    obj = Person.objects.get(pid=k)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/sucess.html",{"obj":obj})




