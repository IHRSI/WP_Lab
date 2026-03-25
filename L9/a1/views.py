from django.shortcuts import render

from .models import Institute


def index(request):
	institutes = Institute.objects.all().order_by('name')
	return render(request, 'a1/index.html', {'institutes': institutes})
