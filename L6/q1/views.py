from django.shortcuts import render
from django.http import HttpRequest

def calculator(request: HttpRequest):
    result = None
    num1 = None
    num2 = None
    operation = None
    error = None
    
    if request.method == 'POST':
        try:
            num1 = int(request.POST.get('num1', 0))
            num2 = int(request.POST.get('num2', 0))
            operation = request.POST.get('operation', 'add')
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    error = "Cannot divide by zero"
                else:
                    result = num1 / num2
        except ValueError:
            error = "Please enter valid integers"
    
    context = {
        'result': result,
        'num1': num1,
        'num2': num2,
        'operation': operation,
        'error': error,
    }
    
    return render(request, 'q1/calculator.html', context)
