from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from math import ceil
from myBakery.models import Contact, Product, Order, OrderUpdate, BirthdayProduct, WeddingProduct
from django.contrib import messages
import json
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# register process
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
            messages.success(request, f'Your account has been created! You are now able to log in')
    else:
        form = UserRegisterForm()
    return render(request, 'myBakery/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'myBakery/profile.html', context)


# Home page
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//3 + ceil((n/3)-(n//3))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'myBakery/index.html',params)


# About page
def about(request):
    return render(request, 'myBakery/about.html')

 # CheckOut page    
def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson','')
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email','')
        address = request.POST.get('address1','')+" "+request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone', default='')
        order = Order( items_json=items_json, fname=fname,lname=lname,email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        print("send orderid " , id, update)
        messages.success( request, 'Order Place!' )
        return render(request, 'myBakery/checkout.html' , {'thank': thank, 'id':id})
    return render( request, 'myBakery/checkout.html',)


# contact page
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Contact details Submitted!')
    return render(request, 'myBakery/contact.html')


# Tracker page
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('error')
        except Exception :
            return HttpResponse('exception')

    return render(request, 'myBakery/tracker.html')


# Product view page
def prodView(request, myid):
    #fetch the product using id
    product = Product.objects.filter(id=myid)
    return render(request, 'myBakery/productView.html', {'product':product[0]})

# Birthday Page
def birthday(request):
    products = BirthdayProduct.objects.all()
    print(products)
    n = len(products)
    nSlides = n//3 + ceil((n/3)-(n//3))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'myBakery/birthdaySpecial.html', params)


# Wedding Page
def wedding(request):
    products = WeddingProduct.objects.all()
    print(products)
    n = len(products)
    nSlides = n//3 + ceil((n/3)-(n//3))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'myBakery/weddingSpecial.html', params)

