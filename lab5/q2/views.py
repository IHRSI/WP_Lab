# Create your views here.
from django.shortcuts import render
from datetime import datetime, date

def home2(request):
    employee_ids = ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005']
    result = None
    
    if request.method == "POST":
        doj_str = request.POST.get('doj')
        
        if doj_str:
            doj = datetime.strptime(doj_str, '%Y-%m-%d').date()
            today = date.today()
            experience = (today - doj).days / 365.25
            
            if experience > 5:
                result = "YES"
            else:
                result = "NO"

    return render(request, 'promotion_form.html', {
        'employee_ids': employee_ids,
        'result': result
    })