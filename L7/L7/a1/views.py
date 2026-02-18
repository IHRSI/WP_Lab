from django.shortcuts import render
from .forms import GroceryForm

GROCERY_ITEMS = {
    '1': {'name': 'Milk', 'price': 50},
    '2': {'name': 'Bread', 'price': 30},
    '3': {'name': 'Eggs', 'price': 60},
    '4': {'name': 'Butter', 'price': 100},
    '5': {'name': 'Cheese', 'price': 150},
    '6': {'name': 'Apple', 'price': 80},
}

def index(request):
    form = GroceryForm()
    return render(request, 'a1/index.html', {'form': form})

def add_items(request):
    if request.method == 'POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            selected_ids = form.cleaned_data['items']
            selected_items = [{'name': GROCERY_ITEMS[id]['name'], 'price': GROCERY_ITEMS[id]['price']} for id in selected_ids]
            return render(request, 'a1/result.html', {'items': selected_items})
    form = GroceryForm()
    return render(request, 'a1/index.html', {'form': form})
