from django import forms
from main.models import Author

class UpdateForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(),required=True, max_length=300)
    class Meta:
        model = Author
        fields = ("fullname", "bio", "profile_pic")
