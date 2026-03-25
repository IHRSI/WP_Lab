from django.shortcuts import redirect, render

from .forms import CategoryForm, PageForm
from .models import Category


def index(request):
	category_form = CategoryForm(prefix='category')
	page_form = PageForm(prefix='page')

	if request.method == 'POST':
		if 'add_category' in request.POST:
			category_form = CategoryForm(request.POST, prefix='category')
			if category_form.is_valid():
				category_form.save()
				return redirect('q1:index')
		elif 'add_page' in request.POST:
			page_form = PageForm(request.POST, prefix='page')
			if page_form.is_valid():
				page_form.save()
				return redirect('q1:index')

	categories = Category.objects.prefetch_related('pages').all().order_by('name')
	context = {
		'category_form': category_form,
		'page_form': page_form,
		'categories': categories,
	}
	return render(request, 'q1/index.html', context)
