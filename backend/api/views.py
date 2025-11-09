from django.shortcuts import render,redirect,HttpResponse
from .models import Category,Item
from .forms import Signup


def handle_request(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    Categories=Category.objects.all()
    return render(request,'index.html',{
        'categories':Categories,
        'items':items
    })

def contact(request):
    return render(request,'contact.html')




def signup(request):
    if request.method=='POST':
        form=Signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form=Signup()
    return render(request,'signup.html',{'form':form})

    
    
    
        


