from django.shortcuts import render,redirect,HttpResponse
from .forms import *

# Create your views here.
def home(request):
    item_data=Items.objects.all()
    context={'item_data':item_data}
    
    return render(request,'index.html',context)


def createitem(request):
    
    item=ItemModelForm()
    if request.method=="POST":
        item=ItemModelForm(request.POST,request.FILES)
        if item.is_valid():
          
            item.save()
          
            return redirect('/home')
        else:
           
            return HttpResponse('Error')
    return render(request,'createitem.html',{'item':item})

def createcategory(request):
    
    category=CategoryModelForm()
    if request.method=="POST":
        category=CategoryModelForm(request.POST,request.FILES)
        if category.is_valid():
          
            category.save()
          
            return redirect('/home')
        else:
           
            return HttpResponse('Error')
    return render(request,'createcategory.html',{'category':category})