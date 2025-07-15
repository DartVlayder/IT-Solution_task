from django.shortcuts import render, redirect
from .models import Quote
from .forms import QuoteForm
import random

def index(request):
    quotes = list(Quote.objects.all())
    quote = None

    if quotes:
        quote = random.choices(quotes, weights=[q.weight for q in quotes])[0]
        quote.views += 1
        quote.save()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QuoteForm()

    return render(request, 'quotes/index.html', {
        'quote': quote,
        'form': form,
    })