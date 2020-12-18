from django.forms import ModelForm, Form
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'text', 'rating']
        exclude = ['author', 'parent_product', 'timestamp']