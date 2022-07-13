from django import forms
from .models import Book,Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
                        'name',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
         
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'category',
            'modarg',

        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_book': forms.FileInput(attrs={'class': 'form-control '}),
            'photo_author': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'modarg': forms.TextInput(attrs={'class': 'form-control'}),

        }