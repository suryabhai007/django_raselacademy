from django import forms
from . models import Comment


class CommentForm(forms.Form):
    author = forms.CharField()
    body = forms.CharField()
    

    def clean_qform(self):
        data = self.cleaned_data['author']
        return data

