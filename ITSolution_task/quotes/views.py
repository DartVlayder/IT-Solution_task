from django.shortcuts import render
from .models import Quote
import random

def index(request):
    quotes = list(Quote.objects.all())

    if quotes:
        quote = random.choices(quotes, weights=[q.weight for q in quotes])[0]
        quote.views += 1
        quote.save()
    else:
        quote = None

    return render(request, 'quotes/index.html', {'quote': quote})
