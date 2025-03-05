from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth


import logging

from customer.models import Addr,Cartinfo,Buyinfo, Orderdetails
# Create your views here.






def registration(request):
    if request.method =='POST':
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        un = request.POST.get('un')
        em = request.POST.get('em')
        pass1 =request.POST.get('pass')
        cpass1 =request.POST.get('cpass')
        if pass1==cpass1:
            if User.objects.filter(username=un).exists():
                messages.error(request,'user alraeady exists use another')
                return redirect('registration')
            else:
                if User.objects.filter(email=em).exists():
                    messages.error(request,'emaillaready exists use another')
                    return redirect('registration')
                else:
                    User.objects.create_user(first_name=fn,last_name=ln,username=un,email=em,password=pass1)
                    return redirect('login')

        else:
            messages.error(request,'password not matched')
            return redirect('registration')
            
    return render(request,'customer/registration.html')



def login(request):
    if request.method == 'POST':
        un=request.POST.get('username')
        pass1= request.POST.get('password')
        User=auth.authenticate(username=un,password=pass1)
        if User is not None:
            auth.login(request,User)
            return redirect('home')
        else:
            messages.error(request,"username and password not valid please  conform are you registered or not")
            return redirect('login')

    return render(request,'customer/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def bestseller(request):
    return render(request,'customer/bestseller.html')



@login_required(login_url='login')
def address(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        pincode = request.POST.get('pincode')
        housename = request.POST.get('housename')
        area = request.POST.get('area')
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        state = request.POST.get('state')
        data = Addr(user=request.user,country=country,name=name,mobile=mobile,pincode=pincode,housename=housename,area=area,landmark=landmark,city=city,state=state)
        data.save()
        return redirect('home')
    
    return render(request,'customer/address.html')


def cartview(request):
    if request.method == 'POST':
        cartimage = request.POST.get('cartimage')
        cartinfo = request.POST.get('cartinfo')
        cartprice = request.POST.get('cartprice')
        quantity = int(request.POST.get('quantity', 1))
        data=Cartinfo(user=request.user,cartimage=cartimage,cartinfo=cartinfo,cartprice=cartprice,quantity=quantity)
        data.save()
        return redirect('cartdata')
    
@login_required(login_url='login')
def cartdata(request):
    cartdata = Cartinfo.objects.filter(user=request.user)
    
    
    quantity = sum(item.quantity for item in cartdata)
    context = {
        'quantity':quantity,
        'cartdata': cartdata,
        
    }
    return render(request, 'customer/cart.html', context)
    

def cartupdate(request,id):
    if request.method == 'POST':
        cartinfo = request.POST.get('cartinfo')
        cartimage = request.POST.get('cartimage')
        cartprice = request.POST.get('cartprice')
        quantity = request.POST.get('quantity')
        data=Cartinfo.objects.get(id=id)
        data.id=id
        data.cartinfo=cartinfo
        data.cartimage=cartimage
        data.cartprice=cartprice
        data.quantity=quantity
        data.save()
        return redirect('cartdata')


def buyview(request):
    if request.method == 'POST':
        buyimage = request.POST.get('buyimage')
        buyinfo = request.POST.get('buyinfo')
        buyprice = request.POST.get('buyprice')
        data=Buyinfo(user=request.user,buyimage=buyimage,buyinfo=buyinfo,buyprice=buyprice)
        data.save()
        return redirect('home')

@login_required(login_url='login')
def buydata(request):
    buydata=Buyinfo.objects.filter(user=request.user)
    context={
        'buydata':buydata,
        
    }
    return render(request,'customer/buydata.html',context)





    

@login_required(login_url='login')
def chekout(request):
    if request.method == 'POST':
        cartitems = Cartinfo.objects.filter(user=request.user)
        for item in cartitems:
            Buyinfo.objects.create(
                user=request.user,
                buyimage=item.cartimage,
                buyinfo=item.cartinfo,
                buyprice=item.cartprice
            )
        cartitems.delete()

        
        return redirect('buydata')
    
    cartitems = Cartinfo.objects.filter(user=request.user)
    quantity = sum(item.quantity for item in cartitems)
    
    customer= Addr.objects.filter(user=request.user)
    
    context = {
        'quantity':quantity,
        'cart_items': cartitems,
        'customer':customer,
    }
    return render(request, 'customer/chekout.html', context)







def orderdetails(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        caddress = request.POST.get('caddress')
        cpincode = request.POST.get('cpincode')
        cmobile = request.POST.get('cmobile')
        cquantity = request.POST.get('cquantity')
        ctotalwithoutgst = request.POST.get('ctotalwithoutgst')
        ctotalwithgst = request.POST.get('ctotalwithgst')
        data=Orderdetails(user=request.user,cname=cname,caddress=caddress,cpincode=cpincode,cmobile=cmobile,cquantity=cquantity,ctotalwithoutgst=ctotalwithoutgst,ctotalwithgst=ctotalwithgst)
        data.save()
        return redirect('chekout')

def delete(request,id):
    data=Cartinfo.objects.filter(id=id)
    data.delete()
    return redirect('cartdata')


