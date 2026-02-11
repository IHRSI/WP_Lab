from django.shortcuts import render

def text_formatter(request):
    context = {
        'name': '',
        'message': '',
        'display_text': '',
        'bold': False,
        'italic': False,
        'underline': False,
        'color': '#000000',
    }
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'display':
            name = request.POST.get('name', '')
            message = request.POST.get('message', '')
            context['name'] = name
            context['message'] = message
            context['display_text'] = f"{name} {message}"
            context['bold'] = request.POST.get('bold') == 'on'
            context['italic'] = request.POST.get('italic') == 'on'
            context['underline'] = request.POST.get('underline') == 'on'
            context['color'] = request.POST.get('color', '#000000')
        
        elif action == 'clear':
            context['name'] = ''
            context['message'] = ''
            context['display_text'] = ''
            context['bold'] = False
            context['italic'] = False
            context['underline'] = False
            context['color'] = '#000000'
    
    return render(request, 'a1/formatter.html', context)
