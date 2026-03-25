from django import forms

from .models import Lives, Works


class LivesForm(forms.ModelForm):
    class Meta:
        model = Lives
        fields = ['person_name', 'street', 'city']


class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['person_name', 'company_name', 'salary']


class CompanySearchForm(forms.Form):
    company_name = forms.CharField(max_length=100)
