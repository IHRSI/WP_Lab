from django.shortcuts import redirect, render

from .forms import ProductForm
from .models import Product


def add_product(request):
	form = ProductForm()
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("q2_index")
	return render(request, "q2/add_product.html", {"form": form})


def index(request):
	products = Product.objects.all()
	return render(request, "q2/index.html", {"products": products})
