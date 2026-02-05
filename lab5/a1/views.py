# Create your views here.
import random
import string
from django.shortcuts import render

def home3(request):
    if request.method == "GET":
        request.session['captcha_text'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        request.session['fail_count'] = 0

    if 'fail_count' not in request.session:
        request.session['fail_count'] = 0

    message = ""
    is_disabled = request.session['fail_count'] >= 3

    if request.method == "POST" and not is_disabled:
        user_input = request.POST.get('captcha_input')
        actual_captcha = request.session.get('captcha_text')

        if user_input == actual_captcha:
            message = "✅ Success! Captcha Matched."
            request.session['fail_count'] = 0

            request.session['captcha_text'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        else:
            request.session['fail_count'] += 1
            message = f"❌ Mismatch! Attempt {request.session['fail_count']} of 3."
            
            if request.session['fail_count'] >= 3:
                is_disabled = True
                message = "🚫 Account Locked: Too many failed attempts."

    return render(request, 'captcha_page.html', {
        'captcha': request.session['captcha_text'],
        'message': message,
        'is_disabled': is_disabled
    })