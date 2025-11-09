from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from api.models import Item


@login_required
def index(request):
    items=Item.objects.filter(created_by=request.user)

    return render(
        request,'dashboard_items.html',{'items':items}
    )
# Create your views here.
