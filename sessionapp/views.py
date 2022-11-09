from django.shortcuts import render
from .forms import namei,surnamei,cityi
# Create your views here.
def name_views(request):
    form=namei()
    return render(request,"name.html",{'form':form})

def surname_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=surnamei()
    return render(request,"surname.html",{"form":form})

def city_view(request):
    surname=request.GET['surname']
    request.session['surname']=surname
    form=cityi()
    return render(request,"city.html",{'form':form})

def result_view(request):
    city=request.GET['city']
    request.session['city']=city

    return render(request,"result.html")