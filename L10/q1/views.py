from django.shortcuts import redirect, render

from .forms import AuthorForm, BookForm, PublisherForm
from .models import Author, Book, Publisher


def index(request):
	author_form = AuthorForm(prefix="author")
	publisher_form = PublisherForm(prefix="publisher")
	book_form = BookForm(prefix="book")

	if request.method == "POST":
		form_type = request.POST.get("form_type")

		if form_type == "author":
			author_form = AuthorForm(request.POST, prefix="author")
			if author_form.is_valid():
				author_form.save()
				return redirect("q1_index")

		elif form_type == "publisher":
			publisher_form = PublisherForm(request.POST, prefix="publisher")
			if publisher_form.is_valid():
				publisher_form.save()
				return redirect("q1_index")

		elif form_type == "book":
			book_form = BookForm(request.POST, prefix="book")
			if book_form.is_valid():
				book_form.save()
				return redirect("q1_index")

	context = {
		"author_form": author_form,
		"publisher_form": publisher_form,
		"book_form": book_form,
		"authors": Author.objects.all(),
		"publishers": Publisher.objects.all(),
		"books": Book.objects.prefetch_related("authors").select_related("publisher"),
	}
	return render(request, "q1/index.html", context)
