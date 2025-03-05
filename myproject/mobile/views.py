from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from customer.models import Cartinfo,Buyinfo
from django.contrib import messages
# from customer.models import cart,Buy

# Create your views here.

def mobile1(request):
    return render(request,'mobile/mobile1.html')
def mobile2(request):
    return render(request,'mobile/mobile2.html')
def mobile3(request):
    return render(request,'mobile/mobile3.html')
def mobile4(request):
    return render(request,'mobile/mobile4.html')









