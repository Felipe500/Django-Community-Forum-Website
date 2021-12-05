from django import forms
from .models import Post,Comment,Author
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags"]

class ComentForm(forms.ModelForm):
    content1 = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30 }))
    
    class Meta:
        model = Post
        fields = []

        
class RespostForm(forms.ModelForm):
    content2 = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30 }))
    
    
    class Meta:
        model = Post
        fields = []

class PerfilForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(), max_length=300,label='Nome completo:')
    bio = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30 }),label='Biografia:')
    profile_pic = forms.ImageField(label='Carregar imagem')
    class Meta:
        model = Author
        fields = ("fullname", "bio", "profile_pic")