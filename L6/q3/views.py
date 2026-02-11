from django.shortcuts import render

def home(request):
    book_data = {
        'title': 'Chemistry',
        'author': 'NCERT',
        'class': '11 CBSE',
        'description': 'Official Chemistry textbook for Class 11 CBSE'
    }
    return render(request, 'q3/home.html', {'book': book_data})

def metadata(request):
    metadata = {
        'isbn': '978-8174502529',
        'pages': 412,
        'edition': 'Latest',
        'language': 'English',
        'published': '2023'
    }
    return render(request, 'q3/metadata.html', {'metadata': metadata})

def reviews(request):
    reviews_list = [
        {'author': 'Student', 'rating': 5, 'text': 'Very comprehensive book with clear explanations.'},
        {'author': 'Teacher', 'rating': 4.5, 'text': 'Great resource for classroom teaching.'},
        {'author': 'Parent', 'rating': 5, 'text': 'Excellent for exam preparation.'}
    ]
    return render(request, 'q3/reviews.html', {'reviews': reviews_list})

def publisher_info(request):
    publisher = {
        'name': 'NCERT Publications',
        'address': 'New Delhi, India',
        'contact': 'publications@ncert.nic.in',
        'website': 'www.ncert.nic.in',
        'description': 'Official publisher of textbooks for Central Board of Secondary Education (CBSE)'
    }
    return render(request, 'q3/publisher_info.html', {'publisher': publisher})
