from django.shortcuts import render, redirect

from app.form import ProductModelForm
from app.models import Product, Category


def index(request):
    products = Product.objects.order_by('-id')
    context = {
        'products':products
    }
    return render(request, 'app/index.html', context)


def product_details(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    context = {
        'product':product
    }
    return render(request, 'app/product_details.html', context)


def shop_view(request):
    return render(request, 'app/shop.html')


def shopping_cart(request):
    return render(request, 'app/shopping_cart.html')


def checkout(request):
    return render(request, 'app/checkout.html')


def contact(request):
    return render(request, 'app/contact.html')


def create_product(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = ProductModelForm()
    context = {
        "form":form,
        "sizes":Product.ChoiceSize,
        "colors":Product.ChoiceColor,
        "categories":category
    }
    return render(request, 'app/create_product.html', context)


def update_product(request, product_id):
    category = Category.objects.all()
    product = Product.objects.filter(id=product_id).first()
    if request.POST == "POST":
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = ProductModelForm(instance=product)
    context = {
        "form":form,
        "sizes": Product.ChoiceSize,
        "colors": Product.ChoiceColor,
        "categories": category
    }
    return render(request, 'app/update_product.html', context)


def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if product:
        product.delete()
    return redirect('index')
