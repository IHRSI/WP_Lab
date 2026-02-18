from django import forms

class GroceryForm(forms.Form):
    ITEM_CHOICES = [
        (1, 'Milk - Rs. 50'),
        (2, 'Bread - Rs. 30'),
        (3, 'Eggs - Rs. 60'),
        (4, 'Butter - Rs. 100'),
        (5, 'Cheese - Rs. 150'),
        (6, 'Apple - Rs. 80'),
    ]
    
    items = forms.MultipleChoiceField(
        choices=ITEM_CHOICES,
        widget=forms.CheckboxSelectMultiple()
    )
