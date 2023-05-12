from django.shortcuts import render
from .models import Quote
import random

def random_quote(request):
    quotes = Quote.objects.all()
    random_quote = random.choice(quotes)
    context = {
        'quote': random_quote
    }
    return render(request, 'random_quote.html', context)
