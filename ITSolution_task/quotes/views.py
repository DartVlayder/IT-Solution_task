from django.shortcuts import render, redirect
from .models import Quote
from .forms import QuoteForm
import random

def index(request):
    quotes = list(Quote.objects.all())
    quote = None

    if request.method == 'POST':
        if 'like_id' in request.POST:
            quote_id = request.POST['like_id']
            quote_to_like = Quote.objects.get(id=quote_id)
            quote_to_like.likes += 1
            quote_to_like.save()
            return redirect('index')

        elif 'dislike_id' in request.POST:
            quote_id = request.POST['dislike_id']
            quote_to_dislike = Quote.objects.get(id=quote_id)
            quote_to_dislike.dislikes += 1
            quote_to_dislike.save()
            return redirect('index')

        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            if quotes:
                quote = random.choices(quotes, weights=[q.weight for q in quotes])[0]

    else:
        form = QuoteForm()
        if quotes:
            quote = random.choices(quotes, weights=[q.weight for q in quotes])[0]
            quote.views += 1
            quote.save()

    return render(request, 'quotes/index.html', {
        'quote': quote,
        'form': form,
    })