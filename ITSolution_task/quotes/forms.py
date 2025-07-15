from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'source', 'weight']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        source = cleaned_data.get('source')

        if text and Quote.objects.filter(text=text).exists():
            self.add_error('text', 'Такая цитата уже существует.')

        if source and Quote.objects.filter(source=source).count() >= 3:
            self.add_error(None, f'У источника «{source}» уже есть 3 цитаты. Нельзя добавить больше.')

        return cleaned_data
