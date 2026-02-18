from django.shortcuts import render, redirect
from .forms import StudentForm

def first_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subject'] = form.cleaned_data['subject']
            return redirect('q2_second_page')
    else:
        form = StudentForm()
    return render(request, 'q2/firstPage.html', {'form': form})

def second_page(request):
    name = request.session.get('name', '')
    roll = request.session.get('roll', '')
    subject = request.session.get('subject', '')
    return render(request, 'q2/secondPage.html', {
        'name': name,
        'roll': roll,
        'subject': subject
    })

def reset_session(request):
    request.session.flush()
    return redirect('q2_first_page')
