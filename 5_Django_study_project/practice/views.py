from django.shortcuts import render
from datetime import datetime
# Create your views here.


def practice_view(request):
    context = {
        'list_of_numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'greeting': "Hello, World!",
        'reversed_greeting': "Hello, World!"[::-1],
        'user_info': {
            'first_name': "John",
            'last_name': "Doe",
            'email': "john.doe@example.com"
        },
        'is_vip': True,
        'notes': "<strong>Note:</strong> Always learn something new!",
        'current_date': datetime.now(),
    }
    return render(request, 'practice/practice_page.html', context)

