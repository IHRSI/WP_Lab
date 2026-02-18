from django import forms

class CarForm(forms.Form):
    MANUFACTURER_CHOICES = [
        ('', 'Choose...'),
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        ('Nissan', 'Nissan'),
        ('BMW', 'BMW'),
    ]
    
    manufacturer = forms.ChoiceField(
        choices=MANUFACTURER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    model = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter car model name'
        })
    )
