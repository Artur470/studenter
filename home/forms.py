from django import forms
from .models import BlogM

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = BlogM
        fields = "__all__"
