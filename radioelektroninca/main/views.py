from django.shortcuts import render, redirect
from .forms import OrderForm
# Create your views here.

def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,'main/about.html')

def contact_us(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = OrderForm()
    context = {
        'form':form
    }
    return render(request,"main/contact_us.html",context)

def reviews(request):
    return render(request,"main/reviews.html")

