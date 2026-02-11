from django.shortcuts import render
from django.http import HttpRequest

def magazine_cover(request: HttpRequest):
    context = {
        'text': '',
        'bg_color': '#ffffff',
        'font_size': '48',
        'font_color': '#000000',
        'font_family': 'Arial',
        'pattern': 'solid',
    }
    
    if request.method == 'POST':
        context['text'] = request.POST.get('text', '')
        context['bg_color'] = request.POST.get('bg_color', '#ffffff')
        context['font_size'] = request.POST.get('font_size', '48')
        context['font_color'] = request.POST.get('font_color', '#000000')
        context['font_family'] = request.POST.get('font_family', 'Arial')
        context['pattern'] = request.POST.get('pattern', 'solid')
    
    return render(request, 'q2/magazine_cover.html', context)
