from django import forms

from stocky.models import Article, Category


class ArticleForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Article
        fields = ['name', 'description', 'serial_number', 'price', 'quantity', 'image', 'categories', 'supplier',
                  'reception_date']
