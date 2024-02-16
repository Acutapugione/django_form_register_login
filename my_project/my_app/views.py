from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from .models import Product
from .forms import ProductForm, ProductFormSet, NewUserCreationForm, LoginForm
from django.contrib.auth import login, logout, authenticate

def login_view(request):
    form = LoginForm(request, data=request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get("username"), 
                                password=form.cleaned_data.get("password"))
            print(f"{user=}")
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, "Login successful.")
                return redirect("index")
        messages.error(request, "Unsuccessful Login.")
    return render(request, "my_app/login.html", context={"form":form})

def register(request):
    form = NewUserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, "Registered successful.")
                return redirect("index")
        messages.error(request, "Unsuccessful registration.")
    return render(request, "my_app/register.html", context={"form":form})

def logout_view(request):
    logout(request)
    
    return redirect("index")

class IndexView(generic.base.TemplateView):
    template_name = "my_app/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        context["form"] = ProductFormSet()
        return context

# Create your views here.
def index(request):
    products = Product.objects.all()

    return render(request, "my_app/index.html", {"products": products})

def create(request):
    form = ProductForm()
    if request.method == "POST":
        new_item = Product(name = request.POST.get("name"))
        new_item.save()
        return redirect("index")
    return render(request, "my_app/create.html", context={"form": form})
