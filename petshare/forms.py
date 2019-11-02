from django import forms
from .models import Post

class new_pet(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['nickname', 'pet_name', 'pet_type', 'comment', 'photo']
