from django.shortcuts import render
from django.http import HttpResponse
from .forms import CarForm

def index(request):
    form = CarForm()
    return render(request, 'q1/index.html', {'form': form})

def result(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            manufacturer = form.cleaned_data['manufacturer']
            model = form.cleaned_data['model']
            return render(request, 'q1/result.html', {
                'manufacturer': manufacturer,
                'model': model
            })
    return HttpResponse("Invalid request")
