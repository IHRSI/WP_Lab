from django.db.models import OuterRef, Subquery
from django.shortcuts import redirect, render

from .forms import CompanySearchForm, LivesForm, WorksForm
from .models import Lives, Works


def index(request):
    lives_form = LivesForm(prefix='lives')
    works_form = WorksForm(prefix='works')
    search_form = CompanySearchForm(prefix='search')
    results = None

    if request.method == 'POST':
        if 'add_lives' in request.POST:
            lives_form = LivesForm(request.POST, prefix='lives')
            if lives_form.is_valid():
                lives_form.save()
                return redirect('q2:index')
        elif 'add_work' in request.POST:
            works_form = WorksForm(request.POST, prefix='works')
            if works_form.is_valid():
                works_form.save()
                return redirect('q2:index')
        elif 'search_company' in request.POST:
            search_form = CompanySearchForm(request.POST, prefix='search')
            if search_form.is_valid():
                company_name = search_form.cleaned_data['company_name']
                lives_city_subquery = Lives.objects.filter(
                    person_name=OuterRef('person_name')
                ).values('city')[:1]
                results = (
                    Works.objects.filter(company_name__iexact=company_name)
                    .annotate(city=Subquery(lives_city_subquery))
                    .values('person_name', 'city')
                )

    context = {
        'lives_form': lives_form,
        'works_form': works_form,
        'search_form': search_form,
        'results': results,
    }
    return render(request, 'q2/index.html', context)
