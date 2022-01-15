from django import forms
from .models import Post,Comment,Author
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    arquivo1 = forms.FileField(label='Carregar Arquivo 1',required=False)
    arquivo2 = forms.FileField(label='Carregar Arquivo 2',required=False)
    arquivo3 = forms.FileField(label='Carregar Arquivo 3',required=False)


    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags",
                  'descricao_arquivo1','arquivo1','descricao_arquivo2','arquivo2','descricao_arquivo3','arquivo3']

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