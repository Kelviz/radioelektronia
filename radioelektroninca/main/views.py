from django.shortcuts import render, redirect
from .forms import OrderForm, FeedbackForm
# Create your views here.

def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,'main/about.html')

def contact_us(request):
    form = OrderForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        'form':form
    }
    return render(request,"main/contact_us.html",context)

def reviews(request):
    form = FeedbackForm(request.POST)
    if request.method == "POST":
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        'form':form
    }
    return render(request,"main/reviews.html",context)

