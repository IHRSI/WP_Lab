from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Student


def index(request):
	form = StudentForm()
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("a1_index")

	students = Student.objects.all()
	return render(request, "a1/index.html", {"form": form, "students": students})
