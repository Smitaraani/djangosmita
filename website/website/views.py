from django.http import HttpResponse

from webapp.models import*
from django.shortcuts import render

def show_about_page(request):
    return render(request,'index.html');




def home_page(request):
    carts= Category.objects.all()
    images= Images.objects.all()
    data = {'images':images,'carts':carts}
    return render(request,'home.html',data)   

def catagory_page(request,cid):

    carts= Category.objects.all()
    category=category.objects.get(pk=cid)
    images= Images.objects.filter(cat=category)
    data = {'images':images,'carts':carts}
    return render(request,'home.html',data)    







