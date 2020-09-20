from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Products

# Create your views here.


def product_list(request):
    context = {'product_list': Products.objects.all()}
    return render(request, "amazon_affiliate/affiliate_list.html", context)


def product_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Products.objects.get(pk=id)
            form = ProductForm(instance=product)
        return render(request, "amazon_affiliate/affiliate_form.html", {'form': form})
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product = Products.objects.get(pk=id)
            form = ProductForm(request.POST,instance= product)
        if form.is_valid():
            form.save()
        return redirect('/list')


def product_delete(request,id):
    product = Products.objects.get(pk=id)
    product.delete()
    return redirect('/list')
