from django.shortcuts import render

def home(request):
    student_data = None
    percentage = None
    
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        english = int(request.POST.get('english', 0))
        physics = int(request.POST.get('physics', 0))
        chemistry = int(request.POST.get('chemistry', 0))
        
        total_marks = english + physics + chemistry
        max_marks = 300
        percentage = round((total_marks / max_marks) * 100, 2)
        
        student_data = f"""Student Name: {name}
Date of Birth: {dob}
Address: {address}
Contact Number: {contact}
Email ID: {email}

--- Marks ---
English: {english}/100
Physics: {physics}/100
Chemistry: {chemistry}/100

Total Marks: {total_marks}/{max_marks}
Percentage: {percentage}%"""
    
    return render(request, 'student_form.html', {
        'student_data': student_data,
        'percentage': percentage
    })