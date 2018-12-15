from django import forms
from microblog import models

class PostCreate(forms.ModelForm):
    class Meta:
        model = models.Post
        #fields = ['title', 'body', 'slug']
        fields = ['title', 'body']


class PostEdit(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body']
